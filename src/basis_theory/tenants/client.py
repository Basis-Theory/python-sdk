# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
from .connections.client import ConnectionsClient
from .invitations.client import InvitationsClient
from .members.client import MembersClient
from .self_.client import SelfClient
from ..core.client_wrapper import AsyncClientWrapper
from .connections.client import AsyncConnectionsClient
from .invitations.client import AsyncInvitationsClient
from .members.client import AsyncMembersClient
from .self_.client import AsyncSelfClient


class TenantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.connections = ConnectionsClient(client_wrapper=self._client_wrapper)
        self.invitations = InvitationsClient(client_wrapper=self._client_wrapper)
        self.members = MembersClient(client_wrapper=self._client_wrapper)
        self.self_ = SelfClient(client_wrapper=self._client_wrapper)


class AsyncTenantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.connections = AsyncConnectionsClient(client_wrapper=self._client_wrapper)
        self.invitations = AsyncInvitationsClient(client_wrapper=self._client_wrapper)
        self.members = AsyncMembersClient(client_wrapper=self._client_wrapper)
        self.self_ = AsyncSelfClient(client_wrapper=self._client_wrapper)
