from django.db import models
# taulua customers vastaava luokka:
class Customers(models.Model):
    CUSTOMER_ROLE = [
        ('light entrepreneur', 'Light Entrepreneur'),
        ('employee', 'Employee'),
    ]
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=False)
    person_id= models.CharField(max_length=250, null=False)
    custom_role = models.CharField(max_length=20, null=False, choices=CUSTOMER_ROLE) # kevytyrittäjä tai työntekijä = light entrepreneur, employee
    tax_number = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=250, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=5, null=False)
    postoffice = models.CharField(max_length=50, null=False)
    tax_rate = models.DecimalField(null=False)
    bankaccount = models.CharField(max_length=18, null=True, blank=True)
    valid_from = models.DateField(null=False)
    valid_to = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.user_id, 
                self.person_id, 
                self.custom_role, 
                self.tax_number, 
                self.last_name, 
                self.first_name, 
                self.email, 
                self.phone, 
                self.address, 
                self.postcode, 
                self.postoffice, 
                self.tax_rate, 
                self.bankaccount, 
                self.valid_from, 
                self.valid_to, 
                self.created, 
                self.updated)


