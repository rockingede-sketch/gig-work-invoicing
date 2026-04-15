from backend.gbsapp.models import BillingCase as bcase
from backend.gbsapp.models import BilligCustomers as bcust
from docs import make_invoice as make_invoice

try:
    inv_case = bcase.objects.get(id=102)
    # haetaan laskutusasiakkaan tiedot:
    billing_cust = bcust.objects.get(id=inv_case.billing_cust_id)
    p_name = billing_cust.name
    p_address = billing_cust.address
    p_zip = billing_cust.postcode
    p_city = billing_cust.postoffice
    p_country = billing_cust.country
    p_business_id = billing_cust.business_id
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