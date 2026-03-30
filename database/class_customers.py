from django.db import models
# taulua customers vastaava luokka:
class Customers(models.Model):
    userId = models.IntegerField(null=False)
    personId= models.CharField(max_length=250, null=False)
    customRole = models.CharField(max_length=20, null=False)
    taxNumber = models.CharField(max_length=20, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=False)
    firstName = models.CharField(max_length=250, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=5, null=False)
    postoffice = models.CharField(max_length=50, null=False)
    taxRate = models.DecimalField(null=False)
    bankaccount = models.CharField(max_length=18, null=True, blank=True)
    validFrom = models.DateField(null=False)
    validTo = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.userId, 
                self.personId, 
                self.customRole, 
                self.taxNumber, 
                self.lastName, 
                self.firstName, 
                self.email, 
                self.phone, 
                self.address, 
                self.postcode, 
                self.postoffice, 
                self.taxRate, 
                self.bankaccount, 
                self.validFrom, 
                self.validTo, 
                self.created, 
                self.updated)


