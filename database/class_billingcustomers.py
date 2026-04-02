from django.db import models
# taulua billingcustomers vastaava luokka:
class BilligCustomers(models.Model):
    CUSTOMER_STATUS_CHOICES = [
        ('valid', 'Valid'),
        ('liquidation', 'Liquidation'),
        ('bankruptcy', 'Bankruptcy'),
        ('defaulter', 'Defaulter'),
        ('ceased_operations', 'Ceased Operations')
    ]
    company_id= models.CharField(max_length=9, null=False)
    company_name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=True)
    contact_person = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=5, null=False)
    postoffice = models.CharField(max_length=50, null=False)
    e_invoice_address = models.CharField(max_length=18, null=True)
    operator_code = models.CharField(max_length=18, null=True)
    customer_status = models.CharField(max_length=20, null=True, choices=CUSTOMER_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.user_id, 
                self.company_id,
                self.company_name,
                self.location, 
                self.email, 
                self.first_name, 
                self.contact_person, 
                self.phone, 
                self.address, 
                self.postcode, 
                self.postoffice, 
                self.e_invoice_address, 
                self.operator_code, 
                self.customer_status, 
                self.created, 
                self.updated)


