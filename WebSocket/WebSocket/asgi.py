"""
ASGI config for WebSocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from  WebSocket import rountings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebSocket.settings")

# application = get_asgi_application()
application=ProtocolTypeRouter({
    "http": get_asgi_application(),#自动找urls.py,找视图函数 --.http
    "websocket":URLRouter(rountings.websocket_urlpatterns),#rountings(相当于urls),consumers(相当于views)
})