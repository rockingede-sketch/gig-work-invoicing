"""
URL configuration for GigBillingSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gbsapp import views as gbsViews
from registration import views as regViews
# from gbsapp.views import sendConfirmEmail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', regViews.home_view, name='homeLink'),
    path('registration/', include('registration.urls',namespace="registration")),
    path("auth/", include("django.contrib.auth.urls")),
    path('laskutus/', gbsViews.laskutus, name='laskutus'),
    path('laskutus/uusi/', gbsViews.lasku_new, name='lasku_new'),
    path('laskutus/uusi/luotu', gbsViews.lasku_new, name='lasku_luotu'),
    path('laskutus/<int:pk>/', gbsViews.lasku_detail, name='lasku_detail')
]

