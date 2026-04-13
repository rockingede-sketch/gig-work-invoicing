from decimal import Decimal

from django.db import models

# taulua paramstable vastaava luokka:
class Paramstable(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=250, null=False)
    valid_from = models.DateField(null=False)
    valid_to = models.DateField(null=True)
    year = models.IntegerField(null=True)
    value = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.description + str(self.year)
# taulua users vastaava luokka:
#class Users(models.Model):
#    username = models.EmailField(max_length=100, null=False)
#    password = models.CharField(max_length=250, null=False)
#    confirmed = models.BooleanField(default=False)
#    valid_from = models.DateField(null=False)
#    valid_to = models.DateField(null=True)
#    disabled = models.BooleanField(default=False)
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)
#
#    def __str__(self):
#        return self.username + ' ' + str(self.confirmed) + ' ' + str(self.disabled)

#Changed the data model, so that we use the native users in django
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    confirmed = models.BooleanField(default=False)
    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.email

# taulua customers vastaava luokka:
class Customer(models.Model):
    CUSTOMER_ROLE = [
        ('light entrepreneur', 'Kevytyrittäjä'),
        ('employee', 'Työntekijä'),
    ]
    #user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='customers')
    person_id= models.CharField(max_length=250, null=False)
    custom_role = models.CharField(max_length=20, null=False, choices=CUSTOMER_ROLE) # kevytyrittäjä tai työntekijä = light entrepreneur, employee
    tax_number = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=250, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=5, null=False)
    postoffice = models.CharField(max_length=50, null=False)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    bankaccount = models.CharField(max_length=18, null=True, blank=True)
    valid_from = models.DateField(null=False)
    valid_to = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

  # taulua companycustomers vastaava luokka:
class CompanyCustomer(models.Model):
    #userId = models.ForeignKey('User', on_delete=models.SET_NULL,null=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='company_customers')
    companyId= models.CharField(max_length=9, null=False)
    email = models.EmailField(max_length=100, null=False)
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
        return self.name
  


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
    email = models.EmailField(max_length=100, null=False)
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
        return str(self.company_name) + ' ' + str(self.location)
    
    # taulua billingcases vastaava luokka:
class BillingCase(models.Model):
    # nämä muuttujat pitää myöhemmin luoda ja hakea Paramastable -luokasta:
    vatfull = Decimal('25.5')
    vatpartial1 = Decimal('13.5')
    vatpartial2 = Decimal('10')
    vat0 = Decimal('0')

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
    VAT_LEVEL = [
        (vatfull, f'ALV {vatfull} %'.replace('.', ',')),
        (vatpartial1, f'ALV {vatpartial1} %'.replace('.', ',')),
        (vatpartial2, f'ALV {vatpartial2} %'.replace('.', ',')),
        (vat0, f'ALV {vat0} %'.replace('.', ',')),
    ]   
    frontman_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name='billingCase_frontman_cust_id')
    billing_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name='billingCase_billing_cust_id')
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
    e_invoice_address = models.CharField(max_length=20, null=True, blank=True)
    payer_reference = models.CharField(max_length=50, null=True, blank=True)
    payment = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    vat_includes = models.BooleanField(default=True, null=False) # bit 0/1
    vat_percent = models.DecimalField(max_digits=5, decimal_places=2, choices=VAT_LEVEL, null=False)
    group_billing = models.BooleanField(default=False, null=False) # bit 0/1
    group_name = models.CharField(max_length=50, null=True, blank=True)
    number_of_members = models.IntegerField(null=False, default=1)
    owner_profit = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.work_description)
    
# taulua billingcaserow vastaava luokka:
class BillingCaseRow(models.Model):
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)  
    frontman = models.BooleanField(default=False, null=False) # bit 0/1
    work_hours = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    share_of_pay = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    other_claims = models.CharField(max_length=500, null=True, blank=True)
    other_claims_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    travel_exp_claim_id = models.IntegerField(null=True, blank=True)
    payroll_id = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.share_of_pay) + ' %'


# taulua contract vastaava luokka:
class Contract(models.Model):

    CONTRACTSTATUS_CHOICES = [
        ('created', 'Created'),
        ('sent', 'Sent'),
        ('not answered', 'Not answered'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=True)
    frontman_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name='Contract_frontman_cust_id')
    billing_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name='contract_billing_cust_id')
    contract_nr = models.CharField(max_length=20, null=False)
    contract_date = models.DateField(null=False)
    last_answer_date = models.DateField(null=False)
    contract_status = models.CharField(max_length=20, null=False, choices=CONTRACTSTATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contract_nr + ' ' + self.contract_status + ' ' + str(self.contract_date) + ' ' + str(self.last_answer_date)

# taulua payroll vastaava luokka:
class Payroll(models.Model):
    PAYMENT_STATE = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ]
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=True)
    billing_case_row_id = models.ForeignKey('BillingCaseRow', on_delete=models.SET_NULL, null=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    customer_role = models.CharField(max_length=20, null=False) # kevytyrittäjä tai työntekijä = light entrepreneur, employee
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
        return str(self.payroll_time) + ' ' + str(self.working_hours) + 'h' + ' ' + str(self.gross_salary) + '€' + ' ' + str(self.net_salary) + '€' + ' ' + str(self.payment_date) + ' ' + self.payment_state
   
# taulua travelexpenceclaim vastaava luokka:
class TravelExpenseClaim(models.Model):
    DAILY_ALLOWANCE_TYPE = [
        ('partial', 'Partial'),
        ('full', 'Full'),
    ]
    PAYMENT_STATE = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ]
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=True)
    billing_case_row_id = models.ForeignKey('BillingCaseRow', on_delete=models.SET_NULL, null=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    travel_begin = models.DateTimeField() # matka alkoi
    travel_ended = models.DateTimeField() # matka päättyi
    country = models.CharField(max_length=50, default='Finland')
    itinerary = models.CharField(max_length=300, null=True, blank=True) # mistä minne
    daily_allowance_type = models.CharField(max_length=10,choices=DAILY_ALLOWANCE_TYPE, null=True, blank=True) # päivärahan tyyppi, osa tai täysi
    daily_allowance_count = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    daily_allowance_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)   
    number_of_km = models.IntegerField(null=True, blank=True) # kilometrit
    price_of_km = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True) # €/km
    price_of_km_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)   # kilometrikorvaus yhteensä
    other_expences_desc = models.CharField(max_length=300, null=True, blank=True) # muuut kulut, selite
    other_expences_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # muut kulut summa
    claims_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) # Matkakulut yhteensä
    payment_date = models.DateField(null=True, blank=True)
    payment_state = models.CharField(max_length=10, default='unpaid', choices=PAYMENT_STATE) # unpaid, paid
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.travel_begin) + ' - ' + str(self.travel_ended) + ' ' + str(self.claims_sum) + '€' + ' ' + str(self.payment_date) + ' ' + self.payment_state

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
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=True)
    billing_cust_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
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
        return self.invoice_num + ' ' + str(self.invoice_date)  + ' ' + str(self.paid_amount) + ' € ' + str(self.payment_date) + ' ' + self.payment_state

# taulua documents vastaava luokka:
class Documents(models.Model):
    DOC_TYPE_CHOICES = [
        ('tax card', 'Tax Card'),
        ('contract', 'Contract'),
        ('accepted contract', 'Accepted Contract'),
        ('invoice', 'Invoice'),
        ('payroll', 'Payroll'),
        ('other appendix', 'Other Appendix'),
    ]

    doc_type = models.CharField(max_length=20, choices=DOC_TYPE_CHOICES, null=False)
    doc_date = models.DateField(null=False)
    # Foreign Keys: 
    #user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='customer')
    contract_id = models.ForeignKey('Contract', on_delete=models.SET_NULL, null=True, blank=True)
    invoice_id = models.ForeignKey('Invoice', on_delete=models.SET_NULL, null=True, blank=True)
    payroll_id = models.ForeignKey('Payroll', on_delete=models.SET_NULL, null=True, blank=True)
    docname = models.CharField(max_length=250, null=False)
    filepath = models.CharField(max_length=250, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.doc_type + ' ' + str(self.doc_date) + ' ' + self.docname
