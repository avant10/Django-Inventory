from django.test import TestCase


class InventoryPageTest(TestCase):
    def test_inventory_page_status_code(self):
        url = '/inventory/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_api_inventory_page_status_code(self):
        url = '/api/inventory/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_page_status(self):
        inventory_id = 1
        url = '/inventory/{inventory_id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)