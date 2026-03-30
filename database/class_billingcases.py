from django.db import models
# taulua billingcases vastaava luokka:
class Customers(models.Model):
    STAGE_CHOICES = [
        ('open', 'Open'),
        ('contract sent', 'Contract Sent'),
        ('contract accepted', 'Contract Accepted'),
        ('contract rejected', 'Contract Rejected'),
        ('assignment', 'Assignment'),
        ('invoice sent', 'Invoice Sent'),
        ('invoice paid', 'Invoice Paid'),
        ('debt collection', 'Debt Collection'),
        ('closed', 'Closed'),
        ('canceled', 'Canceled'),
    ]

    BILLING_METHODS = [
        ('sähköposti', 'Sähköposti'),
        ('verkkolasku', 'Verkkolasku'),
    ]
    frontmanCustId = models.IntegerField(null=False)
    billingCustId = models.IntegerField(null=False)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, null=False)
    jobLocation = models.CharField(max_length=100, null=False)
    jobDate = models.DateField(null=False)
    jobBegin = models.DateTimeField(null=True)
    jobEnded = models.DateTimeField(null=True, blank=True)
    jobHours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    workDescription = models.CharField(max_length=500, null=True, blank=True)
    workTask = models.CharField(max_length=50, null=False)
    contactPerson = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=100, null=False)
    address = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=5, null=True, blank=True)
    postoffice = models.CharField(max_length=50, null=True, blank=True)
    billingMethod = models.CharField(max_length=15, choices=BILLING_METHODS, null=True, blank=True)
    eInvoiceAddress = models.CharField(max_length=18, null=True, blank=True)
    payerReference = models.CharField(max_length=50, null=True, blank=True)
    payment = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    vatPercent = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    groupBilling = models.BooleanField(default=False, null=False) # bit 0/1
    groupName = models.CharField(max_length=50, null=True, blank=True)
    nunberOfMembers = models.IntegerField(null=False, default=1)
    ownerProfit = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.frontmanCustId, 
                self.billingCustId,
                self.stage,
                self.jobLocation, 
                self.jobDate, 
                self.jobBegin,
                self.jobEnded,
                self.jobHours,
                self.workDescription,
                self.workTask,
                self.contactPerson,
                self.phone,
                self.email, 
                self.address,
                self.postcode, 
                self.postoffice,
                self.billingMethod,
                self.eInvoiceAddress,
                self.payerReference,
                self.payment,
                self.vatPercent,
                self.groupBilling,
                self.groupName,
                self.nunberOfMembers,
                self.ownerProfit,
                self.created, 
                self.updated)

