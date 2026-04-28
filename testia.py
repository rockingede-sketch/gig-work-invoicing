import os
import sys
import django
sys.path.append(os.path.join(os.getcwd(), "backend"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.GigBillingSystem.settings')
django.setup()

# Käytä nyt lyhyttä polkua (ilman backend-etuliitettä)
# jotta se täsmää INSTALLED_APPS-asetukseen
from gbsapp.models import BillingCase as bcase
from gbsapp.models import BillingCustomers as bcust
from docs import make_invoice

print("Yhteys muodostettu!")
print(f"BillingCase-rivejä tietokannassa: {bcase.objects.count()}")

try:
    inv_case = bcase.objects.get(id=102)
    # haetaan laskutusasiakkaan tiedot:
    billing_cust = inv_case.billing_cust_id
    p_name = billing_cust.company_name
    p_address = billing_cust.address
    p_zip = billing_cust.postcode
    p_city = billing_cust.postoffice
    p_country = ''
    p_business_id = billing_cust.company_id
    i_service = inv_case.job_date.strftime("%Y-%m-%d") + ", " + inv_case.work_task + ", " + inv_case.work_description + ", " + inv_case.job_location
    i_reference = inv_case.payer_reference
    i_pcs = inv_case.number_of_members
    i_price = inv_case.payment
    i_vat_prec = inv_case.vat_percent
    i_vat_included = inv_case.vat_includes
    i_payer_reference = inv_case.payer_reference

except bcase.DoesNotExist:
    print("Billing case not found")


invoice_values = make_invoice.create_invoice(
    payer_name=p_name,
    payer_address=p_address,
    payer_zip=p_zip,
    payer_city=p_city,
    payer_country=p_country,
    payer_business_id=p_business_id,
    service=i_service,
    pcs=i_pcs,
    price=i_price,
    vat_perc=i_vat_prec,
    vat_included=i_vat_included,
    payer_reference=i_payer_reference
)

print(invoice_values)