from django.urls import path
from . import views
from .views import home_view,register_view,activation_view, profileCompletion_view, dashboard_view
from django.contrib.auth import views as auth_views
from django.urls import re_path

app_name = 'registration'

urlpatterns = [
    path("/", home_view, name="homeLink"),
    path("dashboard/",dashboard_view, name='dashboardLink'),
    path("createAccount/", register_view, name="createAccLink"),
    # path("activate/<uidb64>/<token>/", activation_view, name="activationLink"),
    re_path(
    r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$",
    activation_view,
    name="activationLink"),
    path('profile-complete/', profileCompletion_view, name='profileCompleteLink'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='loginLink'),
    path('logout/',auth_views.LogoutView.as_view(next_page='homeLink'),name='logoutLink'
),
]
