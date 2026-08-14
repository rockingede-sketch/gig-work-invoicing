from django import forms
from .models import BillingCase, Customer, BillingCustomers
from gbsapp.services.customer_info import Asiakas

class HenkiloHakuForm(forms.Form):
    nimi = forms.CharField(
        label='Hae nimellä', 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Kirjoita nimi...'})
    )

class TimePickerInput(forms.TimeInput):
    input_type = 'time'

class BillingCaseForm(forms.ModelForm):
    # Määritellään kentät staattisesti
    customer_info = forms.CharField(
        label='Asiakkaan nimi',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'readonly': 'readonly'}),
        required=False
    )
    customer_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    e_invoice_address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    group_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    number_of_members = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    #billing_cust_id = forms.ModelChoiceField(queryset=BillingCustomers.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    job_begin = forms.TimeField(required=False, input_formats=['%H:%M', '%H.%M'], widget=TimePickerInput(attrs={'class': 'form-control'}), label='Alkoi (klo)')
    job_ended = forms.TimeField(required=False, input_formats=['%H:%M', '%H.%M'], widget=TimePickerInput(attrs={'class': 'form-control'}), label='Päättyi (klo)')

    class Meta:
        model = BillingCase
        # Huom: Poistettu __init__ täältä sisältä, se kuuluu pääluokkaan!
        fields = [
            'job_location', 'job_date', 'job_hours', 'work_description', 'work_task',
            'contact_person', 'phone', 'email', 'address', 'postcode', 'postoffice',
            'billing_method', 'e_invoice_address', 'payer_reference', 'payment',
            'vat_includes', 'vat_percent', 'group_billing', 'group_name', 'number_of_members',
        ]
        labels = {
            'job_location': 'Työpaikan osoite',
            'job_date': 'Työntekopäivämäärä',
            'job_begin': 'Alkoi (klo)',
            'job_ended': 'Päättyi (klo)',
            'job_hours': 'Työtunnit',
            'work_description': 'Työtehtävän kuvaus',
            'work_task': 'Työtehtävä',
            'contact_person':'Yhteyshenkilön nimi:',
            'phone': 'Yhteyshenkilön puhelin',
            'email': 'Yhteyshenkilön sähköposti',
            'address': 'Osoite',
            'postcode': 'Postinumero',
            'postoffice': 'Postitoimipaikka',
            'billing_method': 'Laskutustapa',
            'e_invoice_address': 'Verkkolaskuosoite',
            'payer_reference': 'Maksajan viite',
            'payment': 'Maksu',
            'vat_includes': 'sisältyykö ALV maksuun',
            'vat_percent': 'ALV %',
            'group_billing': 'Ryhmälasku',
            'group_name': 'Ryhmän nimi',
            'number_of_members': 'Jäsenten määrä',
        }
        help_texts = {
            'vat_percent': 'Esim. 25.5 yleinen ALV-kanta',
            'e_invoice_address': 'Pakollinen, jos laskutustapa on verkkolasku',
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
            'vat_includes':     forms.CheckboxInput(attrs={'class': 'form-choice-input'}),
            'vat_percent':      forms.Select(attrs={'class': 'form-select'}),
            'group_billing':    forms.CheckboxInput(attrs={'class': 'form-choice-input'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user and user.is_authenticated:
            try:
                from .models import Customer
                customer = Customer.objects.get(user_id=user.id)
                self.fields['customer_info'].initial = f"{customer.first_name} {customer.last_name}"
                self.fields['c_id'].initial = customer.id
            except Exception:
                pass

    def clean(self):
        cleaned_data = super().clean()
        #billing_method = cleaned_data.get('billing_method')
        #e_invoice = cleaned_data.get('e_invoice_address')
        self.customer_id = cleaned_data.get('customer_id')  # Tallenna customer_id suoraan olioon, jotta se on helposti saatavilla viewsissä
        group_billing = cleaned_data.get('group_billing')
        group_name = cleaned_data.get('group_name')
        num_str = cleaned_data.get('number_of_members')
        number_of_members = int(num_str) if num_str else 1

        #if billing_method == 'verkkolasku' and not e_invoice:
         #   self.add_error('e_invoice_address', 'Pakollinen verkkolaskulle')
        if group_billing and not group_name:
            self.add_error('group_name', 'Työryhmän nimi on pakollinen')
        if group_billing and number_of_members < 2:
            self.add_error('number_of_members', 'Työryhmässä tulee olla vähintään 2 jäsentä')
        return cleaned_data
    
# Maksajan (maksuasiakkaan) tietolomake laskutusasian luomiseen:
class BillingCustomersForm(forms.ModelForm):
    e_invoice_address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    operator_code = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_status = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = BillingCustomers
        fields = [
        'company_name', 
        'location',
        'company_id',
        'contact_person',
        'email',
        'phone',
        'address', 
        'postcode', 
        'postoffice',
        'e_invoice_address',
        'operator_code',  
        'customer_status',
        ]
        labels = {
        'company_name': 'Maksajan nimi',
        'location': 'Toimipaikka/osasto',
        'company_id': 'Y-tunnus',
        'contact_person' : 'Yhteyshenkilö',
        'email': 'Yhteyshenkilön sähköposti',
        'phone': 'Yhteyshenkilön puhelinnumero',
        'address': 'Osoite',
        'postcode': 'Postinumero',
        'postoffice': 'Postitoimipaikka',
        'e_invoice_address': 'Verkkolaskuosoite',
        'operator_code': 'Välittäjätunnus',
        'customer_status': 'Asiakasstatus',
        }
        widgets = {
            'company_name':     forms.TextInput(attrs={'class': 'form-control'}),
            'location':         forms.TextInput(attrs={'class': 'form-control'}),
            'company_id':       forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person':   forms.TextInput(attrs={'class': 'form-control'}),
            'phone':            forms.TextInput(attrs={'class': 'form-control'}),
            'email':            forms.EmailInput(attrs={'class': 'form-control'}),
            'address':          forms.TextInput(attrs={'class': 'form-control'}),
            'postcode':         forms.TextInput(attrs={'class': 'form-control'}),
            'postoffice':       forms.TextInput(attrs={'class': 'form-control'}),                 
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get('location')
        if location == '' or location is None:
            cleaned_data['location'] = None
        e_invoice = cleaned_data.get('e_invoice_address')
        if e_invoice == '' or e_invoice is None:
            cleaned_data['e_invoice_address'] = None
        operator_code = cleaned_data.get('operator_code')
        if operator_code == '' or operator_code is None:
            cleaned_data['operator_code'] = None
        customer_staus = cleaned_data.get('customer_status')
        if customer_staus == '' or customer_staus is None:
            cleaned_data['customer_status'] = 'valid'  # Voidaan asettaa oletuksena, koska asiakas luodaan vain laskutusasiakkaaksi, eikä rekisteröidy itse. Tiedot voidaan päivittää myöhemmin asiakastietolomakkeella.

        return cleaned_data


# Asiakkaan tietojen päivityslomake
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
            'tax_rate': 'Ennakonpidätysprosentti',
            'tax_number': 'Veronumero',
            # 'custom_role' label on jo määritelty ylhäällä
        }
        widgets = {
            'address': forms.TextInput(attrs={'style': 'width: 100%;'}),
        }