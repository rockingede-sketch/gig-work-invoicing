from django.test import TestCase
from django.urls import reverse


class LanguageSelectionTests(TestCase):
    def test_language_selector_changes_django_language(self):
        response = self.client.get("/")
        self.assertContains(response, '<html lang="fi">', html=False)
        self.assertContains(response, "Kirjaudu sisään")
        self.assertRegex(
            response.content.decode(),
            r'(?s)<option\s+value="fi"\s+selected',
        )

        response = self.client.post(
            reverse("set_language"),
            {"language": "en", "next": reverse("homeLink")},
        )
        self.assertRedirects(response, reverse("homeLink"))

        response = self.client.get("/")
        self.assertContains(response, '<html lang="en">', html=False)
        self.assertContains(response, "Log in")
        self.assertContains(response, "Home")
        self.assertContains(response, "Gig Invoicing")
        self.assertRegex(
            response.content.decode(),
            r'(?s)<option\s+value="en"\s+selected',
        )
