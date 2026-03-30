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
    companyId= models.CharField(max_length=9, null=False)
    companyName = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=True)
    contactPerson = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=5, null=False)
    postoffice = models.CharField(max_length=50, null=False)
    eInvoiceAddress = models.CharField(max_length=18, null=True)
    operatorCode = models.CharField(max_length=18, null=True)
    customerStatus = models.CharField(max_length=20, null=True, choices=CUSTOMER_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.userId, 
                self.companyId,
                self.companyName,
                self.location, 
                self.email, 
                self.name, 
                self.contactPerson, 
                self.phone, 
                self.address, 
                self.postcode, 
                self.postoffice, 
                self.eInvoiceAddress, 
                self.operatorCode, 
                self.customerStatus, 
                self.created, 
                self.updated)


