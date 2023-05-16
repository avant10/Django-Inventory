from rest_framework import generics
from inventory.models import Inventory
from .serializers import InventorySerializer

class InventoryAPIView(generics.ListAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = Inventory.objects.select_related('supplier').only('name', 'availability', 'supplier__name')

        # Filter by name if provided as a query parameter
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset