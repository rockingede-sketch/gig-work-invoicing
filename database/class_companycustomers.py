from django.db import models
# taulua companycustomers vastaava luokka:
class CompanyCustomers(models.Model):
    userId = models.ForeignKey('User', on_delete=models.SET_NULL,null=False)
    companyId= models.CharField(max_length=9, null=False)
    email = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=50, null=False)
    contactPerson = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=5, null=False)
    postoffice = models.CharField(max_length=50, null=False)
    bankaccount = models.CharField(max_length=18, null=True)
    validFrom = models.DateField(null=False)
    validTo = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.userId, 
                self.companyId, 
                self.email, 
                self.name, 
                self.contactPerson, 
                self.phone, 
                self.address, 
                self.postcode, 
                self.postoffice, 
                self.bankaccount, 
                self.validFrom, 
                self.validTo, 
                self.created, 
                self.updated)


