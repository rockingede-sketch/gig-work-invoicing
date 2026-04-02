from django.db import models
# taulua billingcaserow vastaava luokka:
class BillingCaseRow(models.Model):
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=False)
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=False)  
    frontman = models.BooleanField(default=False, null=False) # bit 0/1
    work_hours = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    share_of_pay = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    other_claims = models.CharField(max_length=500, null=True, blank=True)
    other_claims_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    travel_exp_claim_id = models.IntegerField(null=True, blank=True)
    pyroll_id = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.billing_case_id, 
                self.customer_id,
                self.frontman,
                self.work_hours,
                self.share_of_pay,
                self.other_claims,
                self.other_claims_amount,
                self.travel_exp_claim_id,
                self.pyroll_id,
                self.created, 
                self.updated)

