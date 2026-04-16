from django.urls import path
from . import views
from .views import home_view,login_view,register_view,createAcc_view,forgotPwd_view, activation_view, profileCompletion_view, dashboard_view
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [
    path("/", home_view, name="homeLink"),
    path("dashboard/",dashboard_view, name='dasboardLink'),
    path("register/", register_view, name="registerLink"),
    path("createAccount/", createAcc_view, name="createAccLink"),
    path("forgotPassword/",forgotPwd_view, name="forgotPwdLink"),
    # path('login/',views.login_view, name="loginLink"),
    path("activate/<uidb64>/<token>/", activation_view, name="activationLink"),
    path('profile-complete/', profileCompletion_view, name='profileCompleteLink'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/loginpage.html'), name='loginLink'),
    path('logout/', auth_views.LogoutView.as_view(), name='logoutLink'),
]

