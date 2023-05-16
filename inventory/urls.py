from django.urls import path, include
from inventory.api.views import InventoryAPIView
from .views import InventoryListView
from .views import InventoryDetailView
from . import views
app_name = 'inventory'

urlpatterns = [
    path('api/inventory/', InventoryAPIView.as_view(), name='api-inventory'),
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),

    
]