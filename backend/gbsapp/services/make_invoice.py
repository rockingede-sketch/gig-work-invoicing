# uv add docxtpl
# uv add docx2pdf
import datetime
from docxtpl import DocxTemplate
from docx2pdf import convert
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "invoicing_case.log"),
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

base_dir = os.path.dirname(os.path.abspath(__file__))

def invoicenumber() -> int:
    # Luodaan hakemisto, jos sitä ei ole
    if not os.path.exists(os.path.join(base_dir, "invoicedata")):
         os.makedirs(os.path.join(base_dir, "invoicedata"))
    # Muodostetaan laskunnumeron vuosi vuoden viimeisistä kahdesta numerosta:
    #nr_start = f'{datetime.datetime.now().year}'.replace("20", "")
    nr_start = str(datetime.datetime.now().year)[2:4]
    # Jos tiedostoa ei ole, luo se ja aseta aloitusarvoksi nr_start + "00001"
    data_dir = os.path.join(base_dir, "invoicedata")
    tiedosto_polku = os.path.join(data_dir, "invoicenumbers.txt")
    if not os.path.exists(tiedosto_polku):
        with open(tiedosto_polku, "w") as f:
            f.write(nr_start + "00001")
    # Lue nykyinen laskunumero, kasvata sitä yhdellä ja tallenna takaisin tiedostoon
    with open(tiedosto_polku, "r") as f:
        luku = int(f.read().strip())
        if str(luku)[:2] != nr_start:
            luku = int(nr_start + "00001")
    # Seuraavan laskun numero ja tallennus
    uusi_luku = luku + 1
    with open(tiedosto_polku, "w") as f:
        f.write(str(uusi_luku))

    return luku

def calculate_reference(invoicenumber: int) -> str:
    """
    Laskee suomalaisen viitenumeron annetusta laskunumerosta. Viitenumero muodostuu laskunumerosta ja tarkistenumerosta, joka lasketaan painotetusta summasta.
    """
    invoice= str(invoicenumber)
    factors = [7, 3, 1]
    sum = 0
    
    # Lasketaan painotettu summa takaperin
    for i, nr in enumerate(reversed(invoice)):
        f = factors[i % 3]
        sum+= int(nr) * f
    
    mark = (10 - (sum % 10)) % 10
    
    return invoicenumber + str(mark)

def create_invoice(payer_name: str, payer_address: str, payer_zip: str, payer_city: str, payer_country: str, payer_business_id: str, service: str, pcs: int, price: float, vat_perc: float, vat_included: bool, payer_reference: str) -> dict:
    # Lataa mallipohja (.docx)
    if not os.path.exists(os.path.join(base_dir, "saved_invoices")):
        os.makedirs(os.path.join(base_dir, "saved_invoices"))

    saved_dir = os.path.join(base_dir, "saved_invoices")
    template_path = os.path.join(base_dir, "Laskupohja.docx")
    word_output = os.path.join(saved_dir, "valmis_lasku.docx")

    invoice_number = str(invoicenumber())
    invoice_date = datetime.datetime.now().strftime("%d.%m.%Y")
    due_date = (datetime.datetime.now() + datetime.timedelta(days=8)).strftime("%d.%m.%Y")
    reference = calculate_reference(invoice_number)
    payer_VAT_id = 'FI' + payer_business_id.replace('-', '')
    if not vat_included:
        price0 = price
        price_vat = price * (1 + vat_perc/100)
    else:
        price_vat = price
        price0 = round(price_vat / (1 + vat_perc/100), 2)

    price_a = round(price0/pcs, 2)
    vat_e = round(price0 * (vat_perc/100), 2)
    price_sum = round(price0, 2)
    vat_sum = vat_e
    total_sum = price_sum + vat_sum

    pdf_output = os.path.join(saved_dir, f"invoice_{payer_business_id}_{invoice_number}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.pdf")
    # Täytä tiedot Word-pohjaan
    try:
        doc = DocxTemplate(template_path)
    
        # laskuun tulevat tiedot
        context = {
            'invoice_number': invoice_number,   
            'invoice_date': invoice_date,  
            'due_date': due_date,
            'reference': reference,  
            'payer_name': payer_name,
            'payer_address': payer_address,
            'payer_zip': payer_zip,
            'payer_city': payer_city,
            'payer_country': '' if payer_country.lower() == 'finland' or payer_country.lower() == 'suomi' or payer_country == '' else payer_country,
            'payer_reference': f'Viitteenne: {payer_reference}' if payer_reference != '' else '',
            'payer_business_id': payer_business_id,
            'payer_VAT_id': payer_VAT_id,
            'service': service, 
            'pcs': pcs,
            'price_a': f"{price_a:.2f}",
            'price': f"{price0:.2f}",
            'vat_perc': f"{vat_perc:.2f} %",
            'vat_e': f"{vat_e:.2f}",
            'price_sum': f"{price_sum:.2f}",
            'vat_sum': f"{vat_sum:.2f}",
            'total_sum': f"{total_sum:.2f}"
        }
    
        doc.render(context)
        doc.save(word_output)
        logging.info(f"Word-tiedosto luotu laskunro {invoice_number}: {word_output}")
        #  Muunnos PDF-muotoon
        convert(word_output, pdf_output)
        logging.info(f"PDF valmis laskunro {invoice_number}: {pdf_output}")

    except Exception as e:
        logging.error(f"Virhe tapahtui: {e}")
    # Palauta laskun tiedot sanakirjana tietokantaan tallennusta varten
    return {
                'invoice_number': invoice_number,
                'invoice_date': invoice_date,
                'due_date': due_date,
                'reference': reference,
                'price': price0,
                'vat_e': vat_e,
                'price_sum': price_sum,
                'vat_sum': vat_sum,
                'total_sum': total_sum,
    }

