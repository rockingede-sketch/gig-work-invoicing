from django.contrib import admin
import gbsapp.models as models
# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.CompanyCustomer)
admin.site.register(models.BillingCustomers)
admin.site.register(models.BillingCase)
admin.site.register(models.Contract)
admin.site.register(models.TravelExpenseClaim)
admin.site.register(models.Paramstable)
admin.site.register(models.UserProfile)
admin.site.register(models.Payroll)