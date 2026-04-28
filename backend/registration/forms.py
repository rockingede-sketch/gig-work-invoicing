from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gbsapp.models import Customer

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adding Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            css = "form-control"

            # If this field has errors, adds Bootstrap's invalid class
            if self.errors.get(field_name):
                css += " is-invalid"

            field.widget.attrs["class"] = css

    # Defines a field‑specific validator for the email field 
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email

    # Override the parent class's(UserCreationForm) save method to set username and email before saving
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]  
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
      
class ProfileCompletionForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name","last_name","person_id","custom_role","tax_number","phone","address",
            "postcode","postoffice","tax_rate","bankaccount"]
        

        