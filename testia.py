import datetime                    
from datetime import datetime
import os
import sys
import django
sys.path.append(os.path.join(os.getcwd(), "backend"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.GigBillingSystem.settings')
django.setup()

# Käytä nyt lyhyttä polkua (ilman backend-etuliitettä)
# jotta se täsmää INSTALLED_APPS-asetukseen
from gbsapp.models import Invoice
from gbsapp.models import BillingCase as bcase
#from gbsapp.models import BillingCustomers as bcust
from docs import make_invoice
import logging

logging.basicConfig(
    level=logging.INFO,
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "invoice_log.log"),
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a')

logging.info("Yhteys muodostettu!")
logging.info(f"BillingCase-rivejä tietokannassa: {bcase.objects.count()}")

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
    logging.info("Billing case not found")


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

invoicing_row = Invoice(
        billing_case_id = inv_case,
        billing_cust_id = billing_cust,
        invoice_num = invoice_values['invoice_number'],
        invoice_date = datetime.strptime(invoice_values['invoice_date'], "%d.%m.%Y").date(),
        due_date = datetime.strptime(invoice_values['due_date'], "%d.%m.%Y").date(),
        invoice_status = 'draft',
        description = i_service,
        salary_sum = None,
        travel_exp_sum = None,
        other_claims_sum = None,
        amount_vat_0 = invoice_values['price'],
        vat_percent = i_vat_prec,
        vat_sum = invoice_values['vat_e'],
        total_amount = invoice_values['total_sum'],  
        reference = invoice_values['reference'],
        bank_account = None,
        paid_amount = 0,
        penalty_interest = None,
        payment_date = None,
        payment_state = 'unpaid'
    )
invoicing_row.save()
