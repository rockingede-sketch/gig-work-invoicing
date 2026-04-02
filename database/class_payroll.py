from django.db import models
# taulua payroll vastaava luokka:
class Payroll(models.Model):
    PAYMENT_STATE = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ]
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=False)
    billing_case_row_id = models.ForeignKey('BillingCaseRow', on_delete=models.SET_NULL, null=False)
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=False)
    # Palkanmaksun tiedot
    payroll_time = models.CharField(max_length=50) # palkanmaksu ajalta
    working_hours = models.DecimalField(max_digits=10, decimal_places=2) # työaika h
    gross_salary = models.DecimalField(max_digits=12, decimal_places=2) # bruttopalkka €
    # Verot ja pidätykset
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2) # ennakonpidätys-%
    tax = models.DecimalField(max_digits=12, decimal_places=2) # ennakonpidätys €
    # Työntekijän omat eläke- työttömyysvakuutusmaksut
    tt_tyel_proc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) # TyEL-vakuutusmaksu-%
    tt_tyel = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # TyEL-vakuutusmaksu €
    tt_tyottvak_proc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) # työttömyysvakuutusmaksu-%
    tt_tyottvak = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # työttömyysvakuutusmaksu €
    net_salary = models.DecimalField(max_digits=12, decimal_places=2) # nettopalkka €
    # Työnantajan maksut
    ta_tyel_proc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) # TyEL-vakuutusmaksu-%
    ta_tyel = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # TyEL-vakuutusmaksu €
    ta_tyottvak_proc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) # työttömyysvakuutusmaksu-%
    ta_tyottvak = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # työttömyysvakuutusmaksu €
    # Tapaturmavakuutusmaksu:
    acc_insur_proc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) # Tapaturmavakuutusmaksu-%
    acc_insur = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # Tapaturmavakuutusmaksu €
    # Maksupäivä ja maksun tila
    payment_date = models.DateField(null=True, blank=True)
    payment_state = models.CharField(max_length=20, default='unpaid', choices=PAYMENT_STATE) # unpaid, paid
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)   


    def __str__(self):
        return (self.id,
                self.billing_case_id, 
                self.billing_case_row_id,
                self.customer_id,
                self.payroll_time,
                self.working_hours,
                self.gross_salary,
                self.tax_rate,
                self.tax,
                self.tt_tyel_proc,
                self.tt_tyel,
                self.tt_tyottvak_proc,
                self.tt_tyottvak,
                self.net_salary,
                self.ta_tyel_proc,
                self.ta_tyel,
                self.ta_tyottvak_proc,
                self.ta_tyottvak,
                self.acc_insur_proc,
                self.acc_insur,
                self.payment_date,
                self.payment_state,
                self.created, 
                self.updated)
    