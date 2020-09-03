from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import Django_Sockets_Test.listener.routing

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': URLRouter(
            Django_Sockets_Test.listener.routing.websocket_urlpatterns
        )
})
