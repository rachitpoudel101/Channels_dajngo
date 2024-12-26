from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django import views
from django.urls import path
from calculator_project import routing

application = ProtocolTypeRouter({
    "http": URLRouter([
        path('', views.calculator_view),  # Routes to your calculator view
    ]),
    "websocket": AuthMiddlewareStack(
        URLRouter(routing.websocket_urlpatterns)
    ),
})
