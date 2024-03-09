from django.core.files import File
from django.test import TestCase
from django.urls import reverse

from .models import *


class MenuItemViewTestCase(TestCase):
    category1 = None
    category2 = None

    @classmethod
    def setUpTestData(cls):
        with open("media/Fast_Food_Picture.jpg", 'rb') as c1:
            image_file_c1 = File(c1)
            cls.category1 = Category.objects.create(
                name='Category1',
                image=image_file_c1
            )

            cls.menu_item1 = MenuItems.objects.create(
                name='Item_1',
                description='This is description for item one',
                is_active=True,
                price=10.99,
                image=image_file_c1,
                category=cls.category1
            )

        with open("media/latte.png", 'rb') as c2:
            image_file_c2 = File(c2)
            cls.category2 = Category.objects.create(
                name='Category2',
                image=image_file_c2
            )

            cls.menu_item2 = MenuItems.objects.create(
                name='Item_2',
                description='THis is description for item two',
                is_active=False,
                price=5.99,
                image=image_file_c2,
                category=cls.category2
            )

    def test_menu_items_list_view_status_code_and_template_used(self):
        response = self.client.get(reverse('menu_items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu_items.html')

    def test_menu_items_list_view_context_contains_menu_items(self):
        response = self.client.get(reverse('menu_items'))
        self.assertIn('menu_items', response.context)

    def test_menu_items_list_view_context_menu_items_count(self):
        response = self.client.get(reverse('menu_items'))
        self.assertEqual(len(response.context['menu_items']), 2)
