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
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,ProfileCompletionForm
from gbsapp.models import Customer,Invoice

# Create your views here.

def home_view(request):
    return render(request, "homepage.html")

def login_view(request):
    return render(request,"registration/loginpage.html")

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
             # Creating inactive user
            # user = form.save(commit=False)
            # user.username = form.cleaned_data['email'] 
            # user.username = form.cleaned_data['username']  
            # user.is_active = False
            # user.save()

            # Generating token + uid
            # uid = urlsafe_base64_encode(force_bytes(user.pk))
            # token = default_token_generator.make_token(user)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            # Building link
            # link = request.build_absolute_uri(
            #     reverse('registration:complete_profile', kwargs={'uidb64': uid, 'token': token})
            # )
                
            domain = get_current_site(request).domain
            link = f"http://{domain}/activate/{uid}/{token}/"

            # subject = "Complete Your Profile - Gig Billing"
            # message = f"Hi {user.first_name},\n\nClick the link below to complete your profile:\n{link}"
            # send_mail(subject, message, None, [user.email])
            
            send_mail(
                "Activate your account",
                f"Click the link: {link}",
                "noreply@gigbillingsystem.com",
                [user.email],
            )

            return render(request, "registration/registrationSuccess.html")
            # return render(request, 'registration/registrationSuccess.html', {'email': user.email})
    else:
        form = RegistrationForm()

    return render(request, "registration/register.html", {"form": form})

def createAcc_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registration:login_view")
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

def activation_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)  # auto login
        return redirect("registration:profileCompleteLink")
    else:
        return HttpResponse("Invalid activation link")

@login_required
def profileCompletion_view(request):
    if Customer.objects.filter(user_id=request.user).exists():
        return redirect("registration:dashboardLink")

    if request.method == "POST":
        form = ProfileCompletionForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.email = request.user.email
            profile.first_name = request.user.first_name
            profile.last_name = request.user.last_name
            profile.valid_from = timezone.now().date()
            profile.save()
            return redirect("registration:dashboardLink")
    else:
        form = ProfileCompletionForm()

    return render(request, "registration/profileComplete.html", {"form": form})

def dashboard_view(request):
    invoices = Invoice.objects.order_by("due_date")[:10]  # show latest 10
    return render(request, "registration/dashboard.html", {"invoices": invoices})