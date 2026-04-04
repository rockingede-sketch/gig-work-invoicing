from django.db import models
# taulua invoices vastaava luokka:
class Invoice(models.Model):
    INVOICE_STATUS = [
        ('draft', 'Draft'),
        ('unsent', 'Unsent'),
        ('sent', 'Sent'),   
        ('disabled', 'Disabled'),
    ]
    PAYMENT_STATE = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('debt_collection', 'Debt Collection'),
    ]
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=False)
    billing_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=False)
    invoice_num = models.CharField(max_length=20, null=False) # laskun numero
    invoice_date = models.DateField(null=False) # laskun päivämäärä
    due_date = models.DateField(null=False) # eräpäivä
    invoice_status = models.CharField(max_length=20, null=False, choices=INVOICE_STATUS) # laskun tila ('draft', 'unsent', 'sent', 'disabled')
    description = models.CharField(max_length=200)
    salary_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # palkkasumma €
    travel_exp_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)  # matkakulusumma €
    other_claims_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # muiden kulujen summa €
    amount_vat_0 = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # laskun summa ilman ALV:tä €
    vat_percent = models.DecimalField(max_digits=5, decimal_places=2) # ALV-prosentti
    vat_sum = models.DecimalField(max_digits=12, decimal_places=2) # ALV:n määrä €
    total_amount = models.DecimalField(max_digits=12, decimal_places=2) # laskun kokonaissumma €
    reference = models.CharField(max_length=30) #  maksun viite
    bank_account = models.CharField(max_length=18, null=True, blank=True) # tilinumero
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # maksettu summa €
    penalty_interest = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # viivästyskorko €
    payment_date = models.DateField(null=True, blank=True) # maksupäivä
    payment_state = models.CharField(max_length=20, null=False) # maksun tila ('paid', 'unpaid', 'debt collection')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id,
                self.billing_case_id, 
                self.billing_cust_id,
                self.invoice_num,
                self.invoice_date,
                self.due_date,
                self.invoice_status,
                self.description,
                self.salary_sum,
                self.travel_exp_sum,
                self.other_claims_sum,
                self.amount_vat_0,
                self.vat_percent,
                self.vat_sum,
                self.total_amount,
                self.reference,
                self.bank_account,
                self.paid_amount,
                self.penalty_interest,
                self.payment_date,
                self.payment_state,
                self.created, 
                self.updated)
               
    