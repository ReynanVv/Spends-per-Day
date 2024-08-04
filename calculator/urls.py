from django.urls import path
from .views import CalculateAPIView

urlpatterns = [
    # URL for listing and creating objects (GET and POST)
    path('calculate/', CalculateAPIView.as_view(), name='calculate-list-create'),

    # URL for retrieving, updating, and deleting a specific object (GET, PUT, DELETE)
    path('calculate/<int:pk>/', CalculateAPIView.as_view(), name='calculate-detail'),
]