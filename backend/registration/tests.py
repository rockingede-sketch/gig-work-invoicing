from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from gbsapp.models import Customer, UserProfile


class LanguageSelectionTests(TestCase):
    def test_create_account_and_profile_completion_pages_are_translated(self):
        response = self.client.get(reverse("registration:createAccLink"))
        self.assertContains(response, "Luo tili")
        self.assertContains(response, "Käyttäjätunnus")
        self.assertContains(response, "Sähköposti")
        self.assertContains(response, "Vahvista salasana")

        user = get_user_model().objects.create_user(
            username="profile-user",
            password="test-password",
        )
        UserProfile.objects.create(user=user, confirmed=False)
        self.client.force_login(user)

        response = self.client.get(reverse("registration:profileCompleteLink"))
        self.assertContains(response, "Viimeistele profiilisi")
        self.assertContains(response, "Henkilötunnus")
        self.assertContains(response, "Tallenna tiedot")
        self.assertContains(response, "Kevytyrittäjä")

        self.client.post(
            reverse("set_language"),
            {"language": "en", "next": reverse("registration:createAccLink")},
        )
        response = self.client.get(reverse("registration:createAccLink"))
        self.assertContains(response, "Create an account")
        self.assertContains(response, "Username")
        self.assertContains(response, "Email")
        self.assertContains(response, "Confirm password")
        self.assertContains(response, "Register")
        self.assertContains(response, "Already have an account?")

        response = self.client.get(reverse("registration:profileCompleteLink"))
        self.assertContains(response, "Complete your profile")
        self.assertContains(response, "Finnish personal identity code")
        self.assertContains(response, "Bank account number (IBAN)")
        self.assertContains(response, "Save details")
        self.assertContains(response, "Light entrepreneur")

        response = self.client.post(
            reverse("registration:profileCompleteLink"),
            {
                "first_name": "Test",
                "last_name": "User",
                "person_id": "010101-123A",
                "custom_role": "light entrepreneur",
                "phone": "123456789",
                "address": "Example street 1",
                "postcode": "00100",
                "postoffice": "Helsinki",
                "tax_rate": "20.00",
            },
        )
        self.assertContains(response, "Profile complete")
        self.assertContains(response, "Your account is now active")
        self.assertContains(response, "View your details")

    def test_password_reset_pages_are_translated(self):
        response = self.client.get(reverse("password_reset"))
        self.assertContains(response, "Unohtunut salasana")
        self.assertContains(response, "Syötä sähköpostiosoitteesi")
        self.assertContains(response, "Lähetä palautuslinkki")

        response = self.client.get(reverse("password_reset_done"))
        self.assertContains(response, "Lähetimme sinulle sähköpostin")

        user = get_user_model().objects.create_user(
            username="reset-user",
            email="reset@example.com",
            password="test-password",
        )
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        confirm_url = reverse(
            "password_reset_confirm",
            kwargs={"uidb64": uidb64, "token": token},
        )
        response = self.client.get(confirm_url, follow=True)
        self.assertContains(response, "Aseta uusi salasana")
        self.assertContains(response, "Uusi salasana")

        response = self.client.get(reverse("password_reset_complete"))
        self.assertContains(response, "Salasana vaihdettu onnistuneesti")
        self.assertContains(response, "Siirry kirjautumiseen")

        invalid_confirm_url = reverse(
            "password_reset_confirm",
            kwargs={"uidb64": uidb64, "token": "invalid-token"},
        )
        response = self.client.get(invalid_confirm_url)
        self.assertContains(response, "Pyydä uusi linkki")

        self.client.post(
            reverse("set_language"),
            {"language": "en", "next": reverse("password_reset")},
        )
        response = self.client.get(reverse("password_reset"))
        self.assertContains(response, "Forgot password")
        self.assertContains(response, "Enter your email address")
        self.assertContains(response, "Send password reset link")

        response = self.client.get(reverse("password_reset_done"))
        self.assertContains(response, "We have emailed you instructions")

        response = self.client.get(confirm_url, follow=True)
        self.assertContains(response, "Set a new password")
        self.assertContains(response, "New password")
        self.assertContains(response, "Reset password")

        response = self.client.get(reverse("password_reset_complete"))
        self.assertContains(response, "Password changed successfully")
        self.assertContains(response, "Go to log in")

        response = self.client.get(invalid_confirm_url)
        self.assertContains(response, "This password reset link is invalid")

    def test_login_page_is_translated(self):
        response = self.client.get(reverse("registration:loginLink"))
        self.assertContains(response, '<html lang="fi">', html=False)
        self.assertContains(response, "Kirjaudu sisään")
        self.assertContains(response, "Käyttäjätunnus")
        self.assertContains(response, "Salasana")
        self.assertContains(response, "Unohtunut salasana?")
        self.assertContains(response, "Eikö sinulla ole tiliä?")

        self.client.post(
            reverse("set_language"),
            {"language": "en", "next": reverse("registration:loginLink")},
        )
        response = self.client.get(reverse("registration:loginLink"))
        self.assertContains(response, '<html lang="en">', html=False)
        self.assertContains(response, "Log in")
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")
        self.assertContains(response, "Forgot your password?")
        self.assertContains(response, "Don't have an account?")
        self.assertContains(response, "Create an account")

    def test_customer_dashboard_is_translated(self):
        user = get_user_model().objects.create_user(
            username="dashboard-user",
            password="test-password",
        )
        UserProfile.objects.create(user=user, confirmed=True)
        Customer.objects.create(
            user_id=user,
            person_id="010101-123A",
            custom_role="light entrepreneur",
            last_name="Example",
            first_name="Test",
            email="test@example.com",
            phone="123456789",
            address="Example street 1",
            postcode="00100",
            postoffice="Helsinki",
            tax_rate=Decimal("20.00"),
            valid_from=timezone.now().date(),
        )
        self.client.force_login(user)

        response = self.client.get(reverse("customer_dashboard"))
        self.assertContains(response, '<html lang="fi">', html=False)
        self.assertContains(response, "Tästä näet omat tietosi")
        self.assertContains(response, "Sukunimi:")
        self.assertContains(response, "Näytä")
        self.assertContains(response, "Kevytyrittäjä")
        self.assertContains(response, "Päivitä tietoja")

        self.client.post(
            reverse("set_language"),
            {"language": "en", "next": reverse("customer_dashboard")},
        )
        response = self.client.get(
            reverse("customer_dashboard"),
            {"show_full": "true"},
        )
        self.assertContains(response, '<html lang="en">', html=False)
        self.assertContains(response, "View your personal details here")
        self.assertContains(response, "Last name:")
        self.assertContains(response, "Hide")
        self.assertContains(response, "Light entrepreneur")
        self.assertContains(response, "Update details")

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
