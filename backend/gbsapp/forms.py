from django import forms
from .models import BillingCase, Customer

class BillingCaseForm(forms.ModelForm):

    e_invoice_address =     forms.CharField(required=False)
    group_name =            forms.CharField(required=False)
    number_of_members =     forms.IntegerField(required=False)

    class Meta:
        model = BillingCase
        labels = {
        'job_location': 'Työn sijainti',
        'job_date': 'Päivämäärä',
        'job_begin': 'Alkoi',
        'job_ended': 'Päättyi',
        'job_hours': 'Tunnit',
        'work_description': 'Kuvaus',
        'work_task': 'Tehtävä',
        'phone': 'Puhelin',
        'email': 'Sähköposti',
        'address': 'Osoite',
        'postcode': 'Postinumero',
        'postoffice': 'Postitoimipaikka',
        'billing_method': 'Laskutustapa',
        'e_invoice_address': 'Verkkolaskuosoite',
        'payer_reference': 'Maksajan viite',
        'payment': 'Maksu (ilman ALV)',
        'vat_includes': 'ALV mukana',
        'vat_percent': 'ALV %',
        'group_billing': 'Ryhmälasku',
        'group_name': 'Ryhmän nimi',
        'number_of_members': 'Jäsenten määrä',
        'front_cust_id': 'Tilaaja',
        'billing_cust_id': 'Laskutusasiakas',
        }

        fields = {
        'job_location',
        'job_date',
        'job_begin',
        'job_ended',
        'job_hours',
        'work_description',
        'work_task',
        'phone',
        'email',
        'address',
        'postcode',
        'postoffice',
        'billing_method',
        'e_invoice_address',
        'payer_reference',
        'payment',
        'vat_includes',
        'vat_percent',
        'group_billing',
        'group_name',
        'number_of_members',
        'front_cust_id',
        'billing_cust_id'
        }

        help_texts = {
        'vat_percent': 'Esim. 25.5 yleinen ALV-kanta',
        'e_invoice_address': 'Pakollinen jos laskutustapa on verkkolasku',
        'payer_reference': 'Maksajan oma viite laskulle',
        } 
        
        widgets = {
        'job_date':         forms.DateInput(attrs={'type': 'date'}),
        'job_begin':        forms.TimeInput(attrs={'type': 'time'}),
        'job_ended':        forms.TimeInput(attrs={'type': 'time'}),
        'work_description': forms.Textarea(attrs={'rows': 3}),
        'group_billing':    forms.CheckboxInput(),
        }
        
        #Automatic Fields:

        #stage
        #created
        #updated
        #owner profit

    def clean(self):
        cleaned_data = super().clean()

        billing_method =    cleaned_data.get('billing_method')
        e_invoice =         cleaned_data.get('e_invoice_address')
        group_billing =     cleaned_data.get('group_billing')
        group_name =        cleaned_data.get('group_name')
        number_of_members  = int(cleaned_data.get('number_of_members') or 0)

        if billing_method == 'verkkolasku' and not e_invoice:
            self.add_error('e_invoice_address', 'Pakollinen verkkolaskulle')

        if group_billing and not group_name:
            self.add_error('group_name', 'Ryhmän nimi on pakollinen')

        if group_billing and number_of_members == 0:
            self.add_error('number_of_members', 'Jäsenten määrä on pakollinen')

        return cleaned_data