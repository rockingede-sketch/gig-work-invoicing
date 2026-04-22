from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gbsapp.models import Customer


class RegistrationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            css = "form-control"

            # If this field has errors, add Bootstrap's invalid class
            if self.errors.get(field_name):
                css += " is-invalid"

            field.widget.attrs["class"] = css

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email

    def save(self, commit=True):
        # user = super().save(commit=False)
        user = super().save(commit=True)
        user.username = self.cleaned_data["email"]  # using email as username
        # user.first_name = self.cleaned_data["first_name"]
        # user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        # user.is_active = False  # IMPORTANT
        if commit:
            user.save()
        return user
    
class ProfileCompletionForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["person_id","custom_role","tax_number","phone","address",
            "postcode","postoffice","tax_rate","bankaccount"]
        

        