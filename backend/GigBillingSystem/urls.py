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
from django.urls import path
from gbsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('sendconfirmation/', sendConfirmEmail.as_view(), name='send-confirmation-email'),
    path('forms/group_billing/', views.group_billing_fields, name='group_billing_fields'),
    path('forms/e_invoice_address/', views.e_invoice_address, name='e_invoice_address_fields'),
    path('laskutus/', views.laskutus, name='laskutus'),
    path('laskutus/uusi/', views.lasku_new, name='lasku_new'),
    path('laskutus/uusi/luotu', views.lasku_new, name='lasku_luotu'),
    path('laskutus/<int:pk>/', views.lasku_detail, name='lasku_detail'),
    path('customer/<int:userid>/', views.customer_dashboard, name='customer_dashboard'),
    path('customer/<int:userid>/edit/', views.update_customer, name='update_customer'),

]