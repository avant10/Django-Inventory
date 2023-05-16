from django.shortcuts import render
from django.views import View
import requests
from django.views.generic.detail import DetailView
from .models import Inventory

class InventoryListView(View):
    template_name = 'inventory/inventory_list.html'
    api_url = 'http://localhost:8000/api/inventory'

    def get(self, request):
        response = requests.get(self.api_url)
        inventories = response.json()
        return render(request, self.template_name, {'inventories': inventories})

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    context_object_name = 'inventory'