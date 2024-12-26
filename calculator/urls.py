from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator_view, name='calculator'),  # Main calculator page
    path('calculate/', views.calculate_view, name='calculate'),  # Calculation endpoint
]
