from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self) -> None:
        Menu.objects.create(title="Ice Cream", price=1.9, inventory=100)
        Menu.objects.create(title="Hamburger", price=3.9, inventory=100)
        Menu.objects.create(title="Hot Dog", price=2.4, inventory=100)

    def test_getAll(self):
        menu_items = Menu.objects.all()
        menu_items_deserialized = MenuSerializer(menu_items, many=True).data

        self.assertEqual(3, len(menu_items_deserialized))
