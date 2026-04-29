from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.http import HttpResponse
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,ProfileCompletionForm
from gbsapp.models import Customer,Invoice,UserProfile

# Create your views here.

def home_view(request):
    return render(request, "homepage.html")

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Calling RegistrationForm class's save method
            user = form.save(commit=False)
            # Saving the user record as inactive in the User model
            user.is_active = False 
            user.save()

            # Creates user profile row 
            UserProfile.objects.create(user=user)
                      
            # Generate activation token
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # print("Decoded UID:", uid)

            token = account_activation_token.make_token(user)

            # Build activation link
            activation_url = reverse(
                "registration:activationLink",
                kwargs={"uidb64": uid, "token": token}
            )
            domain = get_current_site(request).domain
            activation_link = f"http://{domain}{activation_url}"

            # Send activation email
           
            send_mail(
                "Activate your account",
                f"Click the link:\n\n{activation_link}\n",
                "keikkalaskutus@gmail.com",
                [user.email],
            )

            return render(request, "registration/registrationSuccess.html",{"email": form.cleaned_data["email"]})
        else:
            print("FORM ERRORS:", form.errors)  # Debugging
    else:
        form = RegistrationForm()

    return render(request, "registration/createAccount.html", {"form": form})
    
def activation_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        # print("UIDB64:", uidb64)
        # print("Decoded:", urlsafe_base64_decode(uidb64))

    except:
        user = None

    if user and account_activation_token.check_token(user, token):
        # Making the user active
        user.is_active = True
        user.save()
        return render(request,"registration/ActivationSuccess.html")
    else:
        return HttpResponse("Failed to send an activation link email. Please retry.")

# Saving profile data to the Customer model
def profileCompletion_view(request):
    # if Customer.objects.filter(user_id=request.user).exists():
    if request.user.profile.confirmed:
        print("Record already exists in Customer model")
        return redirect("registration:dashboardLink")

    if request.method == "POST":
        form = ProfileCompletionForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.email = request.user.email
            profile.valid_from = timezone.now().date()
            profile.user_id = request.user
            profile.save()
            
            request.user.profile.confirmed = True
            request.user.profile.save()
            
            return render(request, "registration/profileComplete.html")
    else:
        form = ProfileCompletionForm()

    return render(request, "registration/completeProfile.html", {"form": form})

def dashboard_view(request):
    userProfile = getattr(request.user, "profile", None)

    if not userProfile or not userProfile.confirmed:
        return redirect("registration:profileCompleteLink")
    else:
        return render(request, "registration/dashboard.html")