from django.db import models
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
    billing_case_id = models.ForeignKey('BillingCase', on_delete=models.SET_NULL, null=False)
    billing_case_row_id = models.ForeignKey('BillingCaseRow', on_delete=models.SET_NULL, null=False)
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=False)
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
        return (self.id,
                self.billing_case_id, 
                self.billing_case_row_id,
                self.customer_id,
                self.travel_begin,
                self.travel_ended,
                self.country,
                self.itinerary,
                self.daily_allowance_type,
                self.daily_allowance_count,
                self.daily_allowance_amount,
                self.number_of_km,
                self.price_of_km,
                self.price_of_km_sum,
                self.other_expences_desc,
                self.other_expences_sum,
                self.claims_sum,
                self.payment_date,
                self.payment_state,
                self.created, 
                self.updated)
    