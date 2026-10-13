from django.test import TestCase
from django.urls import reverse


class CustomerURLTests(TestCase):
    def test_update_customer_url_does_not_require_user_id(self):
        self.assertEqual(reverse("update_customer"), "/customer/edit/")
