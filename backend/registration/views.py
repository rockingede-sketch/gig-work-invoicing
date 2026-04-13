from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from .forms import RegistrationForm, ProfileCompletionForm

# Create your views here.

def home_view(request):
    return render(request, "homepage.html")

def login_view(request):
    return render(request,"registration/loginpage.html")

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Creating inactive user
            user = form.save(commit=False)
            user.username = form.cleaned_data['email'] 
            # user.username = form.cleaned_data['username']  
            user.is_active = False
            user.save()

            # Generating token + uid
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            # Building link
            link = request.build_absolute_uri(
                reverse('accounts:complete_profile', kwargs={'uidb64': uid, 'token': token})
            )

            # Sending email
            subject = "Complete Your Profile - Gig Billing"
            message = f"Hi {user.first_name},\n\nClick the link below to complete your profile:\n{link}"
            send_mail(subject, message, None, [user.email])

            return render(request, 'accounts/registration_success.html', {'email': user.email})
    else:
        form = RegistrationForm()

    return render(request, "registration/register.html", {"form": form})

def createAcc_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_view")
    else:
        form = RegistrationForm()

    return render(request, "registration/createAccount.html", {"form": form})


def forgotPwd_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # You can integrate Django's password reset system here
        return redirect("login")

    return render(request, "registration/forgotPwd.html")

User = get_user_model()

def completeProfile_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    # Validating token
    if user is None or not default_token_generator.check_token(user, token):
        return render(request, 'registration/invalidLink.html')

    # If POST, saves profile data and activates user
    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST)
        if form.is_valid():
            # Saving extra data (for now, storing in user model temporarily)
            # user.profile_phone = form.cleaned_data['phone']
            # user.profile_address = form.cleaned_data['address']

            # Activate user
            user.is_active = True
            user.save()

            return render(request, 'registration/profileCompleted.html')
    else:
        form = ProfileCompletionForm()

    return render(request, 'registration/completeProfile.html', {'form': form, 'user': user})
