from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from taxi.models import Manufacturer, Car


class SearchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user", password="password123"
        )
        cls.man_1 = Manufacturer.objects.create(name="Toyota", country="Japan")
        cls.man_2 = Manufacturer.objects.create(name="Tesla", country="USA")

    def setUp(self):
        self.client.force_login(self.user)

    def test_manufacturer_search_by_name(self):
        url = reverse("taxi:manufacturer-list")
        response = self.client.get(url, {"title": "toy"})

        self.assertEqual(len(response.context["manufacturer_list"]), 1)
        self.assertContains(response, "Toyota")
        self.assertNotContains(response, "Tesla")
