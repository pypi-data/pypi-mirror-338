import asyncio

# Server Mode:
import importlib.resources
import json
import logging
import os
import uuid
from datetime import datetime
from importlib.metadata import version
from typing import Callable

from ariadne import (
    MutationType,
    QueryType,
    ScalarType,
    SchemaDirectiveVisitor,
    make_executable_schema,
)
from ariadne.asgi import GraphQL
from dateutil import parser
from gql import Client
from gql import gql as gql_client
from gql.transport.aiohttp import AIOHTTPTransport
from graphql import FieldDefinitionNode, GraphQLError

from .app_types import (
    ApiKey,
    LinkConfirmation,
    NewIntent,
    NewOfferCall,
    NewOfferCallable,
    NewOfferCallableCostResponse,
    NewOfferCallResponse,
    NewOfferReference,
    NewOfferReferenceCostResponse,
    NewOfferResponse,
    NewSkill,
    OfferCall,
    OfferCallable,
    OfferCallableCostRequest,
    OfferReference,
    OfferReferenceCostRequest,
    OfferRequest,
    PALinkUrl,
    PALocationRequest,
    PALocationResponse,
    PANewConversation,
    PAPaymentRequest,
    PASupportRequest,
    PAUserMessage,
    PAUserResponse,
    PaymentRequest,
    Response,
    Skill,
    Url,
)

DATA_CHUNK_SIZE = 1024 * 1024  # 1 MB in bytes


class Maoto:
    class ServerMode:
        class AuthDirective(SchemaDirectiveVisitor):
            def visit_field_definition(self, field: FieldDefinitionNode, _) -> FieldDefinitionNode:
                original_resolver = field.resolve

                async def resolve_auth(root, info, **kwargs):
                    """Authenticate and authorize API key."""

                    request = info.context["request"]
                    value = request.headers.get("Authorization")

                    if not value:
                        raise GraphQLError("Authentication failed. No API key provided.")
                    if value in ["marketplace_apikey_value", "assistant_apikey_value"]:
                        info.context["apikey"] = ApiKey(
                            id=uuid.uuid4(),
                            time=datetime.now(),
                            user_id=uuid.uuid4(),
                            name=value,
                            roles=[],
                            url=None,
                        )
                    else:
                        raise GraphQLError("Wrong apikey value.")

                    return await original_resolver(root, info, **kwargs)

                field.resolve = resolve_auth
                return field

        def __init__(
            self,
            logger: logging.Logger,
            resolver: Callable[[object], None],
            debug: bool,
        ):
            self.logger, self.resolver, self.debug = logger, resolver, debug

            self.query, self.mutation = QueryType(), MutationType()
            self.scalars = [
                ScalarType(name, serializer=serializer, value_parser=parser_)
                for name, (serializer, parser_) in {
                    "Datetime": (lambda v: v.isoformat(), lambda v: parser.parse(v)),
                    "DICTSTR": (json.dumps, json.loads),
                    "UUID": (str, uuid.UUID),
                }.items()
            ]

            mutation_mappings = {
                "callOffer": OfferCall,
                "requestCallableOfferCost": OfferCallableCostRequest,
                "requestReferenceOfferCost": OfferReferenceCostRequest,
                "requestOffers": OfferRequest,
                "forwardResponse": Response,
                "forwardPaymentRequest": PaymentRequest,
                "forwardLinkConfirmation": LinkConfirmation,
                "forwardPAPaymentRequest": PAPaymentRequest,
                "forwardPALocationRequest": PALocationRequest,
                "forwardPAUserMessage": PAUserMessage,
                "forwardPALinkUrl": PALinkUrl,
            }

            for field_name, model_class in mutation_mappings.items():

                @self.mutation.field(field_name)
                async def resolver(_, info, input: dict[str, object], model_class=model_class):
                    instance = model_class(**input)
                    asyncio.create_task(self.resolver(instance))
                    return True

            schema_str = (importlib.resources.files(__package__) / "agent.graphql").read_text()
            self.executable_schema = make_executable_schema(
                schema_str,
                [self.query, self.mutation] + self.scalars,
                directives={"auth": self.AuthDirective},
            )

            self.graphql_app = GraphQL(
                self.executable_schema,
                debug=self.debug,
            )

    class GraphQLService:
        def __init__(self, url: str, apikey_value: str, schema=None, version: str = "undefined"):
            self._url, self._apikey_value, self._schema, self._version = (
                url,
                apikey_value,
                schema,
                version,
            )

        def _get_client(self, server_url: str) -> Client:
            transport = AIOHTTPTransport(
                ssl=True,
                url=server_url,
                headers={"Authorization": self._apikey_value, "Version": self._version},
            )
            client = Client(
                transport=transport,
                fetch_schema_from_transport=False,
                schema=self._schema,
            )
            return client

        async def execute_async(self, query, variable_values=None):
            gql_client = self._get_client(self._url)
            return await gql_client.execute_async(query, variable_values=variable_values)

    def __init__(
        self,
        logging_level=None,
        assistant=True,
        marketplace=True,
        apikey_value: str | None = None,
    ):
        self._apikey = None

        # Set up logging and debug mode
        self._debug = (
            os.getenv("DEBUG", "False").lower() == "true"
            or os.getenv("MAOTO_DEBUG", "False").lower() == "true"
        )
        # Set up logging
        self._logging_level = (
            logging_level if logging_level else logging.DEBUG if self._debug else logging.INFO
        )
        logging.basicConfig(
            level=self._logging_level,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        self.logger = logging.getLogger(__name__)
        # Disable INFO logs for gql and websockets
        logging.getLogger("gql").setLevel(logging.DEBUG if self._debug else logging.WARNING)
        logging.getLogger("websockets").setLevel(logging.DEBUG if self._debug else logging.WARNING)

        self._domain_mp = os.environ.get("DOMAIN_MP", "mp.maoto.world")
        self._domain_pa = os.environ.get("DOMAIN_PA", "pa.maoto.world")

        self._use_ssl = os.environ.get("USE_SSL", "true").lower() == "true"
        self._protocol = "https" if self._use_ssl else "http"
        self._port_mp = os.environ.get("PORT_MP", "443" if self._use_ssl else "80")
        self._port_pa = os.environ.get("PORT_PA", "443" if self._use_ssl else "80")

        self._url_mp = self._protocol + "://" + self._domain_mp + ":" + self._port_mp + "/graphql"
        self._url_pa = self._protocol + "://" + self._domain_pa + ":" + self._port_pa + "/graphql"

        self._protocol_websocket = "wss" if self._use_ssl else "ws"
        self._url_marketplace_subscription = self._url_mp.replace(
            self._protocol, self._protocol_websocket
        )

        self._apikey_value = apikey_value or os.environ.get("MAOTO_API_KEY")
        if not self._apikey_value:
            raise ValueError("API key is required.")

        self._handler_registry = dict()

        if assistant:
            self._graphql_service_assistant = self.GraphQLService(
                url=self._url_pa,
                apikey_value=self._apikey_value,
                version=version("maoto-agent"),
            )

        if marketplace:
            self._graphql_service_marketplace = self.GraphQLService(
                url=self._url_mp,
                apikey_value=self._apikey_value,
                version=version("maoto-agent"),
            )

        self._server = self.ServerMode(self.logger, self._resolve_event, self._debug)
        self.handle_request = self._server.graphql_app.handle_request

    async def _resolve_event(self, event_obj: object):
        event = type(event_obj)
        if event in self._handler_registry:
            self._handler_registry[event](event_obj)
        else:
            self.logger.warning(f"No handler registered for event type {event}")

    async def _get_own_api_key(self) -> ApiKey:
        # Query to fetch the user's own API keys, limiting the result to only one
        query = gql_client("""
        query {
            getOwnApiKeys {
                apikey_id
                user_id
                name
                time
                roles
            }
        }
        """)

        result = await self._graphql_service_marketplace.execute_async(query)
        data_list = result["getOwnApiKeys"]

        # Return the first API key (assume the list is ordered by time or relevance)
        if data_list:
            data = data_list[0]
            return ApiKey(**data)
        else:
            raise Exception("No API keys found for the user.")

    async def get_own_api_key(self) -> ApiKey:
        """
        Retrieve and cache the current API key.

        Returns
        -------
        ApiKey
            The API key associated with this agent instance.
        """
        if not self._apikey:
            self._apikey = await self._get_own_api_key()
        return self._apikey

    async def check_status_marketplace(self) -> bool:
        """
        Check if the Marketplace service is available.

        Returns
        -------
        bool
            True if the Marketplace is operational, False otherwise.
        """
        query = gql_client("""
        query {
            checkStatus
        }
        """)
        result = await self._graphql_service_marketplace.execute_async(query)
        return result["checkStatus"]

    async def check_status_assistant(self) -> bool:
        """
        Check if the Assistant service is available.

        Returns
        -------
        bool
            True if the Assistant is operational, False otherwise.
        """
        query = gql_client("""
        query {
            checkStatus
        }
        """)
        result = await self._graphql_service_assistant.execute_async(query)
        return result["checkStatus"]

    async def send_intent(self, new_intent: NewIntent) -> None:
        """
        Send an Intent object to the Marketplace for resolution.

        Parameters
        ----------
        new_intent : NewIntent
            The Intent object to create.
        """
        query = gql_client("""
        mutation createIntent($input: NewIntent!) {
            createIntent(input: $input)
        }
        """)
        await self._graphql_service_marketplace.execute_async(
            query, variable_values={"input": new_intent.model_dump()}
        )

    async def unregister(
        self,
        obj: Skill | OfferCallable | OfferReference | None = None,
        obj_type: type[Skill | OfferCallable | OfferReference] | None = None,
        id: uuid.UUID | None = None,
        solver_id: uuid.UUID | None = None,
    ) -> bool:
        """
        Unregister an existing Skill, OfferCallable, or OfferReference from the Marketplace to make it unavailable for use.

        Parameters
        ----------
        obj : Skill or OfferCallable or OfferReference or None, optional
            The object to unregister.
        obj_type : type, optional
            The type of object to unregister.
        id : uuid.UUID, optional
            The ID of the object to unregister.
        solver_id : uuid.UUID, optional
            The ID of the object to unregister.

        Returns
        -------
        bool
            True if the object was successfully unregistered.

        Raises
        ------
        ValueError
            If required parameters are missing or the object type is unsupported.
        """
        if obj:
            obj_type, obj_id = type(obj), obj.id
        elif obj_type and (id or solver_id):
            obj_id = id or solver_id
        else:
            raise ValueError("Either obj or obj_type and id/solver_id must be provided.")

        if obj_type == Skill:
            query = gql_client("""
                mutation unregisterSkill($skill_id: ID!) {
                    unregisterSkill(skill_id: $skill_id)
                }
            """)
            variable_values = {"skill_id": str(obj_id)}
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values=variable_values
            )
            return result["unregisterSkill"]

        elif obj_type == OfferCallable:
            query = gql_client("""
                    mutation unregisterOfferCallable($offercallable_id: ID!) {
                        unregisterOfferCallable(offercallable_id: $offercallable_id)
                    }
                """)
            variable_values = {"offercallable_id": str(obj_id)}
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values=variable_values
            )
            return result["unregisterOfferCallable"]

        elif obj_type == OfferReference:
            query = gql_client("""
                mutation unregisterOfferReference($offerreference_id: ID!) {
                    unregisterOfferReference(offerreference_id: $offerreference_id)
                }
            """)
            variable_values = {"offerreference_id": str(obj_id)}
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values=variable_values
            )
            return result["unregisterOfferReference"]

        else:
            raise ValueError(f"Object type {obj_type} not supported.")

    async def send_response(
        self,
        obj: NewOfferResponse
        | NewOfferCallResponse
        | NewOfferCallableCostResponse
        | NewOfferReferenceCostResponse,
    ) -> bool:
        """
        Send a response object to the Marketplace to complete a request or update its status.

        Parameters
        ----------
        obj : NewOfferResponse or NewOfferCallResponse or NewOfferCallableCostResponse or NewOfferReferenceCostResponse
            The response object to send. One of:

            - **NewOfferResponse**
              Sent in response to an `OfferRequest`.
              Informs the marketplace of the offers made when an intent matches a registered skill.

            - **NewOfferCallResponse**
              Sent in response to an `OfferCall`.
              Informs the caller of status updates related to the offer call.

            - **NewOfferCallableCostResponse**
              Sent in response to an `OfferCallableCostRequest` (when cost is `None`).
              Informs the marketplace of the actual cost for a callable offer.

            - **NewOfferReferenceCostResponse**
              Sent in response to an `OfferReferenceCostRequest` (when cost or URL is `None`).
              Informs the marketplace of the cost and/or URL for a reference offer.

        Returns
        -------
        bool
            True if the response was successfully sent.

        Raises
        ------
        ValueError
            If the object type is unsupported.
        """
        if isinstance(obj, NewOfferCallResponse):
            query = gql_client("""
            mutation sendOfferCallResponse($input: OfferCallResponse!) {
                sendOfferCallResponse(input: $input)
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values={"input": obj.model_dump()}
            )
            return result["sendOfferCallResponse"]

        if isinstance(obj, NewOfferResponse):
            query = gql_client("""
            mutation sendOfferResponse($input: OfferResponse!) {
                sendOfferResponse(input: $input)
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values={"input": obj.model_dump()}
            )
            return result["sendOfferResponse"]

        elif isinstance(obj, NewOfferCallableCostResponse):
            query = gql_client("""
            mutation sendNewOfferCallableCostResponse($input: NewOfferCallableCostResponse!) {
                sendNewOfferCallableCostResponse(input: $input)
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values={"input": obj.model_dump()}
            )
            return result["sendOfferCallableCostResponse"]

        elif isinstance(obj, NewOfferReferenceCostResponse):
            query = gql_client("""
            mutation sendNewOfferReferenceCostResponse($input: NewOfferReferenceCostResponse!) {
                sendNewOfferReferenceCostResponse(input: $input)
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values={"input": obj.model_dump()}
            )
            return result["sendOfferReferenceCostResponse"]

        else:
            raise ValueError(f"Object type {type(obj)} not supported.")

    async def register(self, obj: NewSkill | NewOfferCallable | NewOfferReference) -> bool:
        """
        Register a new Skill, OfferCallable, or OfferReference with the Marketplace to make it available.

        Parameters
        ----------
        obj : NewSkill or NewOfferCallable or NewOfferReference
            The object to register. One of:

            - **NewSkill**
              Lists the skills the agent can react to when an intent matches.
              Enables the marketplace to prompt the agent to resolve `OfferRequests`
              with `OfferResponses` when the intent matches the skill.

            - **NewOfferCallable**
              Lists an OfferCallable the agent can resolve.
              Enables the marketplace to:
                - Resolve `OfferCallableCostRequests` with `OfferCallableCostResponses` (when cost is `None`)
                - Resolve `OfferCalls` with `OfferCallResponses`

            - **NewOfferReference**
              An NewOfferReference the agent links to.
              Enables the marketplace to:
                - Resolve `OfferReferenceCostRequests` with `OfferReferenceCostResponses` (when cost or URL is `None`)
                - Resolve `OfferCalls` with `OfferCallResponses`

        Returns
        -------
        bool
            True if the object was successfully registered.
        """
        if isinstance(obj, NewSkill):
            query = gql_client("""
            mutation registerSkill($input: NewSkill!) {
                registerSkill(input: $input)
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values={"input": obj.model_dump()}
            )
            return result["registerSkill"]

        elif isinstance(obj, NewOfferCallable):
            query = gql_client("""
            mutation registerOfferCallable($input: NewOfferCallable!) {
                registerOfferCallable(input: $input)
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values={"input": obj.model_dump()}
            )
            return result["registerOfferCallable"]

        elif isinstance(obj, NewOfferReference):
            query = gql_client("""
            mutation registerOfferReference($input: NewOfferReference!) {
                registerOfferReference(input: $input)
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(
                query, variable_values={"input": obj.model_dump()}
            )
            return result["registerOfferReference"]

    async def get_registered(
        self, type_ref: Skill | OfferCallable | OfferReference
    ) -> list[Skill | OfferCallable | OfferReference]:
        """
        Retrieve registered objects of a specified type from the Marketplace.

        Parameters
        ----------
        type_ref : Skill or OfferCallable or OfferReference
            The type of object to retrieve.

        Returns
        -------
        list of Skill or OfferCallable or OfferReference
            A list of registered objects of the specified type.

        Raises
        ------
        ValueError
            If the provided type is not supported.
        """
        if type_ref == Skill:
            query = gql_client("""
            query {
                getSkills {
                    id
                    time
                    description
                    tags
                }
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(query)
            return [Skill(**data) for data in result["getSkills"]]

        elif type_ref == OfferCallable:
            query = gql_client("""
            query {
                getOfferCallables {
                    id
                    time
                    parameters
                    description
                    tags
                    followup
                    cost
                }
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(query)
            return [OfferCallable(**data) for data in result["getOfferCallables"]]

        elif type_ref == OfferReference:
            query = gql_client("""
            query {
                getOfferReferences {
                    id
                    time
                    url
                    description
                    tags
                    followup
                    cost
                }
            }
            """)
            result = await self._graphql_service_marketplace.execute_async(query)
            return [OfferReference(**data) for data in result["getOfferReferences"]]

    async def refund_offercall(
        self, offercall: OfferCall | None = None, id: uuid.UUID | None = None
    ) -> bool:
        """
        Refund an OfferCall in case of an error or other issues. This might also be in case the user asks to cancel the OfferCall.

        Parameters
        ----------
        offercall : OfferCall or None, optional
            The OfferCall object to refund.
        id : uuid.UUID, optional
            The ID of the OfferCall to refund.

        Returns
        -------
        bool
            True if the OfferCall was successfully refunded.

        Raises
        ------
        ValueError
            If required parameters are missing.
        """
        offercall_id = (offercall.id if offercall else None) or id
        if not offercall_id:
            raise ValueError("Either offercall or id must be provided.")

        query = gql_client("""
        mutation refundOfferCall($offer_call_id: ID!) {
            refundOfferCall(offer_call_id: $offer_call_id)
        }
        """)
        result = await self._graphql_service_marketplace.execute_async(
            query, variable_values={"offer_call_id": str(offercall_id)}
        )
        return result["refundOfferCall"]

    async def send_newoffercall(self, new_offercall: NewOfferCall) -> OfferCall:
        """
        Sends a new OfferCall to the Marketplace / Agent.

        Parameters
        ----------
        new_offercall : NewOfferCall
            The OfferCall object to create.

        Returns
        -------
        OfferCall
            The created OfferCall object.

        Raises
        ------
        ValueError
            If the OfferCall object is invalid.
        """
        query = gql_client("""
        mutation createNewOfferCall($input: NewOfferCall!) {
            createNewOfferCall(input: $input) {
                id
                time
                apikey_id
                offer_id
                deputy_apikey_id
                parameters
            }
        }
        """)
        return OfferCall(**(
            await self._graphql_service_marketplace.execute_async(
                query, variable_values={"input": new_offercall.model_dump()}
            )
        )["createNewOfferCall"])

    async def set_webhook(self, url: str = None):
        """
        Set or update the webhook URL associated with the agent's API key.

        Parameters
        ----------
        url : str, optional
            The webhook URL to be set. If not provided, the value is retrieved from the
            MAOTO_AGENT_URL environment variable.

        Raises
        ------
        ValueError
            If neither a `url` argument nor the MAOTO_AGENT_URL environment variable is provided.
        """
        if not url:
            env_url = os.getenv("MAOTO_AGENT_URL")
            if not env_url:
                raise ValueError("No URL provided in environment variable MAOTO_AGENT_URL.")
            url = Url(env_url)

        query = gql_client("""
        mutation addUrlToApikey($url: String!) {
            addUrlToApikey(urls: $url)
        }
        """)

        result = await self._graphql_service_marketplace.execute_async(
            query, variable_values={"url": url}
        )

    def register_handler(
        self,
        event: OfferCall
        | OfferRequest
        | OfferCallableCostRequest
        | OfferReferenceCostRequest
        | Response
        | PaymentRequest
        | LinkConfirmation,
    ):
        """
        Register a handler function for a specific event type.

        Parameters
        ----------
        event : OfferCall or OfferRequest or OfferCallableCostRequest or OfferReferenceCostRequest or Response or PaymentRequest or LinkConfirmation
            The event type to register a handler for.

        Returns
        -------
        function
            The decorator function to register the handler.

        Raises
        ------
        ValueError
            If the event type is not supported
        """

        def decorator(func):
            self._handler_registry[event] = func
            return func

        return decorator

    async def send_to_assistant(
        self,
        obj: PALocationResponse | PAUserResponse | PANewConversation | PASupportRequest,
    ):
        """
        Send a supported object to the Assistant service via a GraphQL mutation.

        Parameters
        ----------
        obj : PALocationResponse or PAUserResponse or PANewConversation or PASupportRequest
            The object to forward to the Assistant service.

        Raises
        ------
        GraphQLError
            If the provided object type is not supported.
        """
        if isinstance(obj, PALocationResponse):
            value_name = "pa_locationresponse"
            query = gql_client("""
                mutation forwardPALocationResponse($pa_locationresponse: PALocationResponse!) {
                    forwardPALocationResponse(pa_locationresponse: $pa_locationresponse)
                }
            """)
        elif isinstance(obj, PAUserResponse):
            value_name = "pa_userresponse"
            query = gql_client("""
                mutation forwardPAUserResponse($pa_userresponse: PAUserResponse!) {
                    forwardPAUserResponse(pa_userresponse: $pa_userresponse)
                }
            """)
        elif isinstance(obj, PANewConversation):
            value_name = "pa_newconversation"
            query = gql_client("""
                mutation forwardPANewConversation($pa_newconversation: PANewConversation!) {
                    forwardPANewConversation(pa_newconversation: $pa_newconversation)
                }
            """)
        elif isinstance(obj, PASupportRequest):
            value_name = "pa_supportrequest"
            query = gql_client("""
                mutation forwardPASupportRequest($pa_supportrequest: PASupportRequest!) {
                    forwardPASupportRequest(pa_supportrequest: $pa_supportrequest)
                }
            """)
        else:
            raise GraphQLError(f"Object type {type(obj).__name__} not supported.")

        await self._graphql_service_assistant.execute_async(
            query, variable_values={value_name: obj.model_dump()}
        )
