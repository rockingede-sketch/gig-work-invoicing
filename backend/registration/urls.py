from django.urls import path
from . import views
from .views import home_view,login_view,register_view,createAcc_view,forgotPwd_view
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [
    path("", home_view, name="homeLink"),

    path("register/", views.register_view, name="registerLink"),
    path("createAccount/", views.createAcc_view, name="createAccLink"),
    path("forgotPassword/", views.forgotPwd_view, name="forgotPwdLink"),
    # path('login/',views.login_view, name="loginLink"),
    path('complete-profile/<uidb64>/<token>/', views.completeProfile_view, name='completeProfileLink'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/loginpage.html'), name='loginLink'),
    path('logout/', auth_views.LogoutView.as_view(), name='logoutLink'),
]



# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('complete-profile/<uidb64>/<token>/', views.complete_profile, name='complete_profile'),
#     path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]