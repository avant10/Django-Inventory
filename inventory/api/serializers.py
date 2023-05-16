from rest_framework import serializers
from inventory.models import Inventory, Supplier

class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name')

    class Meta:
        model = Inventory
        fields = ['name', 'supplier_name', 'availability']