from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LanguageSelectionTests(TestCase):
    def test_language_selector_changes_django_language(self):
        response = self.client.get("/")
        self.assertContains(response, '<html lang="fi">', html=False)
        self.assertContains(response, "Helppo ja nopea tapa laskuttaa ilman omaa yritystä")
        self.assertContains(response, "Aloita laskutus muutamassa minuutissa")
        self.assertContains(response, "Aloita nyt")
        self.assertContains(response, "Nopea laskutus")
        self.assertContains(response, 'alt="Laskun luominen"', html=False)
        self.assertContains(response, "Kirjaudu sisään")
        self.assertNotContains(response, "Omat tietosi")
        self.assertNotContains(response, 'href="/laskutus/"', html=False)
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
        self.assertContains(
            response,
            "An easy and fast way to invoice without your own company",
        )
        self.assertContains(response, "Start invoicing in just a few minutes")
        self.assertContains(response, "Get started")
        self.assertNotContains(response, "Your details")
        self.assertNotContains(response, 'href="/laskutus/"', html=False)
        self.assertContains(response, "Fast invoicing")
        self.assertContains(response, "Create an invoice in minutes and send it to your customer.")
        self.assertContains(response, "No paperwork")
        self.assertContains(
            response,
            "We take care of taxes, insurance, and other obligations for you.",
        )
        self.assertContains(response, "A secure service")
        self.assertContains(response, "A reliable Finnish invoicing service.")
        self.assertContains(response, 'alt="Invoice creation"', html=False)
        self.assertContains(response, "Log in")
        self.assertContains(response, "Home")
        self.assertContains(response, "Gig Invoicing")
        self.assertRegex(
            response.content.decode(),
            r'(?s)<option\s+value="en"\s+selected',
        )


class HomepageNavigationTests(TestCase):
    def test_authenticated_user_sees_account_navigation(self):
        user = get_user_model().objects.create_user(
            username="test-user",
            password="test-password",
        )
        self.client.force_login(user)

        response = self.client.get("/")

        self.assertContains(response, "Omat tietosi")
        self.assertContains(response, 'href="/laskutus/"', html=False)
