from django.urls import path
from . import views
from .views import home_view,register_view,forgotPwd_view, activation_view, profileCompletion_view, dashboard_view
from django.contrib.auth import views as auth_views
from django.urls import re_path

app_name = 'registration'

urlpatterns = [
    path("/", home_view, name="homeLink"),
    path("dashboard/",dashboard_view, name='dashboardLink'),
    path("createAccount/", register_view, name="createAccLink"),
    # path("createAccount/register/", register_view, name="registerLink"),
    # path("createAccount/", createAcc_view, name="createAccLink"),
    path("forgotPassword/",forgotPwd_view, name="forgotPwdLink"),
    # path('login/',views.login_view, name="loginLink"),
    # path("activate/<uidb64>/<token>/", activation_view, name="activationLink"),
    re_path(
    r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$",
    activation_view,
    name="activationLink"),
    path('profile-complete/', profileCompletion_view, name='profileCompleteLink'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/loginpage.html'), name='loginLink'),
    path('logout/', auth_views.LogoutView.as_view(), name='logoutLink'),
]

