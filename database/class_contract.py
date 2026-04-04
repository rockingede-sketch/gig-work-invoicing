from django.db import models
# taulua contract vastaava luokka:
class Contract(models.Model):

    CONTRACTSTATUS_CHOICES = [
        ('created', 'Created'),
        ('sent', 'Sent'),
        ('not answered', 'Not answered'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=False)
    frontman_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=False)
    billing_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=False)
    contract_nr = models.CharField(max_length=20, null=False)
    contract_date = models.DateField(null=False)
    last_answer_date = models.DateField(null=False)
    contract_status = models.CharField(max_length=20, null=False, choices=CONTRACTSTATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.billing_case_id, 
                self.customer_id,
                self.frontman_cust_id,
                self.billing_cust_id,
                self.contract_nr,
                self.contract_date,
                self.last_answer_date,
                self.contract_status,
                self.created, 
                self.updated)

