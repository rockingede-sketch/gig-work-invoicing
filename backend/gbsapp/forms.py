from django import forms
from .models import BillingCase, Customer, BillingCustomers

class TimePickerInput(forms.TimeInput):
    input_type = 'time'

class BillingCaseForm(forms.ModelForm):

    e_invoice_address = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    group_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    number_of_members = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'class':'form-control'}))
    
    billing_cust_id = forms.ModelChoiceField(queryset=BillingCustomers.objects.all(),widget=forms.Select(attrs={'class': 'form-select'}))
    
    front_cust_id = forms.ModelChoiceField(queryset=Customer.objects.all(),widget=forms.Select(attrs={'class': 'form-select'}))

    job_begin = forms.TimeField(required=False,input_formats=['%H:%M', '%H.%M'],widget=TimePickerInput(attrs={'class': 'form-control'}))
    
    job_ended = forms.TimeField(required=False,input_formats=['%H:%M', '%H.%M'],widget=TimePickerInput(attrs={'class': 'form-control'}))

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
        'contact_person':'Henkilo Nimi:',
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

        fields = [
        'job_location',
        'job_date',
        'job_begin',
        'job_ended',
        'job_hours',
        'work_description',
        'work_task',
        'contact_person',
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
        ]

        help_texts = {
        'vat_percent': 'Esim. 25.5 yleinen ALV-kanta',
        'e_invoice_address': 'Pakollinen jos laskutustapa on verkkolasku',
        'payer_reference': 'Maksajan oma viite laskulle',
        } 
        
        widgets = {
            'job_location':     forms.TextInput(attrs={'class': 'form-control'}),
            'job_date':         forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'job_hours':        forms.NumberInput(attrs={'class': 'form-control'}),
            'work_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'work_task':        forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person':   forms.TextInput(attrs={'class': 'form-control'}),
            'phone':            forms.TextInput(attrs={'class': 'form-control'}),
            'email':            forms.EmailInput(attrs={'class': 'form-control'}),
            'address':          forms.TextInput(attrs={'class': 'form-control'}),
            'postcode':         forms.TextInput(attrs={'class': 'form-control'}),
            'postoffice':       forms.TextInput(attrs={'class': 'form-control'}),
            'billing_method':   forms.Select(attrs={'class': 'form-select'}),
            'payer_reference':  forms.TextInput(attrs={'class': 'form-control'}),
            'payment':          forms.NumberInput(attrs={'class': 'form-control'}),
            'vat_includes':     forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'vat_percent':      forms.Select(attrs={'class': 'form-select'}),
            'group_billing':    forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
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
    
class CustomerUpdateForm(forms.ModelForm):
    # Ylikirjoitetaan kenttä tässä, jotta voimme pakottaa valinnat ilman tyhjää
    custom_role = forms.ChoiceField(
        label='Asiakasrooli',
        widget=forms.RadioSelect(attrs={'class': 'no-bullets'}),
        choices=[
            ('light entrepreneur', 'Kevytyrittäjä'),
            ('employee', 'Työntekijä')
        ],
        required=True  # Tämä poistaa automaattisesti "---------" vaihtoehdon
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Nyt init-metodissa ei tarvitse enää kikkailla empty_labelin kanssa

    class Meta:
        model = Customer
        fields = [
            'last_name', 'first_name', 
            'phone', 'address', 'postcode', 'postoffice', 
            'bankaccount', 'tax_rate', 'tax_number', 'custom_role'
        ]
        labels = {
            'last_name': 'Sukunimi',
            'first_name': 'Etunimi',
            'phone': 'Puhelinnumero',
            'address': 'Katuosoite',
            'postcode': 'Postinumero',
            'postoffice': 'Postitoimipaikka',
            'bankaccount': 'Tilinumero (IBAN)',
            'tax_rate': 'Veroprosentti',
            'tax_number': 'Veronumero',
            # 'custom_role' label on jo määritelty ylhäällä
        }
        widgets = {
            'address': forms.TextInput(attrs={'style': 'width: 100%;'}),
        }