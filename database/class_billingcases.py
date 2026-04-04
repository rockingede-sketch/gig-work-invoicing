from django.db import models
# taulua billingcases vastaava luokka:
class BillingCases(models.Model):
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
    frontman_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=False)
    billing_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=False)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, null=False)
    job_location = models.CharField(max_length=100, null=False)
    job_date = models.DateField(null=False)
    job_begin = models.DateTimeField(null=True)
    job_ended = models.DateTimeField(null=True, blank=True)
    job_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    work_description = models.CharField(max_length=500, null=True, blank=True)
    work_task = models.CharField(max_length=50, null=False)
    contact_person = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=100, null=False)
    address = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=5, null=True, blank=True)
    postoffice = models.CharField(max_length=50, null=True, blank=True)
    billing_method = models.CharField(max_length=15, choices=BILLING_METHODS, null=True, blank=True)
    e_invoice_address = models.CharField(max_length=18, null=True, blank=True)
    payer_reference = models.CharField(max_length=50, null=True, blank=True)
    payment = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    vat_percent = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    group_billing = models.BooleanField(default=False, null=False) # bit 0/1
    group_name = models.CharField(max_length=50, null=True, blank=True)
    number_of_members = models.IntegerField(null=False, default=1)
    owner_profit = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.frontman_cust_id, 
                self.billing_cust_id,
                self.stage,
                self.job_location, 
                self.job_date, 
                self.job_begin,
                self.job_ended,
                self.job_hours,
                self.work_description,
                self.work_task,
                self.contact_person,
                self.phone,
                self.email, 
                self.address,
                self.postcode, 
                self.postoffice,
                self.billing_method,
                self.e_invoice_address,
                self.payer_reference,
                self.payment,
                self.vat_percent,
                self.group_billing,
                self.group_name,
                self.number_of_members,
                self.owner_profit,
                self.created, 
                self.updated)

