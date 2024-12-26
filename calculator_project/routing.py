from django.urls import path
from calculator.consumers import CalculatorConsumer

websocket_urlpatterns = [
    path('ws/calculate/', CalculatorConsumer.as_asgi()),
]
