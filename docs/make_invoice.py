# uv add docxtpl
# uv add docx2pdf
import datetime
from docxtpl import DocxTemplate
from docx2pdf import convert
import os
# Lataa mallipohja (.docx)
base_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(base_dir, "Laskupohja.docx")
word_output = os.path.join(base_dir, "valmis_lasku.docx")
pdf_output = os.path.join(base_dir, "valmis_lasku.pdf")

invoice_number = '2026-001'
invoice_date = datetime.datetime.now().strftime("%d.%m.%Y")
due_date = (datetime.datetime.now() + datetime.timedelta(days=8)).strftime("%d.%m.%Y")
payer_name = 'Sepen Kapakka tmi'
payer_address = 'Hämäräkuja 2'
payer_zip = '00100'
payer_city = 'Helsinki'
payer_country = ''
payer_business_id = '1234567-8'
payer_VAT_id = 'FI' + payer_business_id.replace('-', '')
service = 'Eskon ja Nickin laulu ja soitto 1 tunti 30.3.2026'
pcs = 1
price = 1999.40
total_price = pcs * price
vat_perc = 25.50
vat_e = total_price * (vat_perc/100)
price_sum = total_price
vat_sum = vat_e
total_sum = price_sum + vat_sum
# 2. Täytä tiedot Word-pohjaan
try:
    doc = DocxTemplate(template_path)
    
    # Tähän tiedot, jotka haluat laskuun
    context = {
        'invoice_number': invoice_number,   
        'invoice_date': invoice_date,  
        'due_date': due_date,     
        'payer_name': payer_name,
        'payer_address': payer_address,
        'payer_zip': payer_zip,
        'payer_city': payer_city,
        'payer_country': payer_country,
        'payer_business_id': payer_business_id,
        'payer_VAT_id': payer_VAT_id,
        'service': service, 
        'pcs': pcs,
        'price': f"{price:.2f}",
        'tot_price': f"{total_price:.2f}",
        'vat_perc': f"{vat_perc:.2f} %",
        'vat_e': f"{vat_e:.2f}",
        'price_sum': f"{price_sum:.2f}",
        'vat_sum': f"{vat_sum:.2f}",
        'total_sum': f"{total_sum:.2f}"
    }
    
    doc.render(context)
    doc.save(word_output)
    print(f"Word-tiedosto luotu: {word_output}")

    # 3. Muunnos PDF-muotoon
    print("Muunnetaan PDF-muotoon... (Tämä avaa Wordin taustalla)")
    convert(word_output, pdf_output)
    print(f"PDF valmis: {pdf_output}")

except Exception as e:
    print(f"Virhe tapahtui: {e}")