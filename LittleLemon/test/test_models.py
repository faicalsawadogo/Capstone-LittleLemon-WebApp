from django.test import TestCase
from booking.models import Menu


class MenuTestCase(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(name='Menu item 1', price = 12.50, menu_item_description='Menu item 1')
        
        self.assertEqual(menu.name, 'Menu item 1')
        self.assertEqual(menu.price, 12.50)
        self.assertEqual(menu.menu_item_description, 'Menu item 1')
        self.assertEqual(str(menu), 'Menu item 1 : 12.50')