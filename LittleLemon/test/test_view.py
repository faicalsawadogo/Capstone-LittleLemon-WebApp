from django.test import TestCase
from littlelemonapi.models import MenuItem
from littlelemonapi.serializers import MenuSerializer
class MenuItemViewTest(TestCase):

    def setUp(self):
        MenuItem.objects.create(name='Menu Item 1', price=8.99, menu_item_description='Menu item 1')
        MenuItem.objects.create(name='Menu Item 2', price=5.99, menu_item_description='Menu item 2')

    def test_getall(self):
        menus = MenuItem.objects.all()
        serializer = MenuSerializer(menus, many=True)
        serialized_data = serializer.data
        response = self.client.get('/api/menu-items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)