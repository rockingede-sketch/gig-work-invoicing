from django.shortcuts import render
from gbsapp.models import BillingCase
from gbsapp.models import Invoice
from django.db.models import Sum, Q
from django.utils import timezone
from datetime import datetime
from datetime import timedelta
from .forms import BillingCaseForm
from django.shortcuts import redirect
from .services.services import BillingCalculators
from django.http import HttpResponse
from .services import make_invoice
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "invoice_log.log"),
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a')

def laskutus(request):

    filter_status = str(request.GET.get('status'))

    #All Invoices
    invoices = BillingCase.objects.all()
    invoice_total_count = invoices.count()

    #Open invoices
    open_invoices = invoices.filter(stage__in=['open', 'contract sent', 'contract accepted', 'assignment', 'invoice sent'])
    open_count = open_invoices.count()
    open_total = open_invoices.aggregate(t=Sum('payment'))['t'] or 0

    #Late Payment invoices
    late_invoices = invoices.filter(stage='invoice sent',created__date__lt=timezone.now().date() - timedelta(days=14))
    late_count = late_invoices.count()
    late_total = late_invoices.aggregate(t=Sum('payment'))['t'] or 0

    #Paid invoices
    paid_invoices = invoices.filter(stage='invoice paid')
    paid_count = paid_invoices.count()
    paid_total = paid_invoices.aggregate(t=Sum('payment'))['t'] or 0
    
    #Decide what invoices to pass to the context
    if filter_status == 'open':
        invoices = open_invoices
    elif filter_status == 'paid':
        invoices = paid_invoices
    elif filter_status == 'late':
        invoices = late_invoices

    context = {
        'invoices' : invoices,
        'status_filter': filter_status,
        'total_count': invoice_total_count,
        'open_count': open_count,
        'late_count': late_count,
        'late_total': late_total,
        'paid_count': paid_count,
        'open_total': open_total,
        'paid_total': paid_total,
    }

    return render(request, 'gbsapp/laskutus/laskutus.html',context)

def lasku_new(request):
    if request.method == 'POST':
        lasku_form = BillingCaseForm(request.POST)
       
        
        if lasku_form.is_valid():
             
            job_date = lasku_form.cleaned_data.get('job_date')
            job_begin_time = lasku_form.cleaned_data.get('job_begin')
            job_ended_time = lasku_form.cleaned_data.get('job_ended')

            uusi_lasku = lasku_form.save(commit=False)
            uusi_lasku.stage = 'open'

            if job_date and job_begin_time:
                uusi_lasku.job_begin = datetime.combine(job_date, job_begin_time)
            
            if job_date and job_ended_time:
                uusi_lasku.job_ended = datetime.combine(job_date, job_ended_time)

            uusi_lasku.owner_profit = BillingCalculators.calculate_customer_portion(
                uusi_lasku.payment,
                uusi_lasku.number_of_members or 1
            )
            uusi_lasku.save()
            #return redirect('lasku_luotu', pk=uusi_lasku.pk)
            return redirect('lasku_luotu')
    else:
        lasku_form = BillingCaseForm()

    return render(request, 'gbsapp/laskutus/lasku_new.html', {'form': lasku_form})

         
def lasku_luotu(request):
    return render(request, 'gbsapp/laskutus/lasku_new_confirm.html')
    

def lasku_detail(request, pk):
    invoice = BillingCase.objects.get(pk=pk)
    return render(request, 'gbsapp/laskutus/lasku_detail.html', {'invoice': invoice})

def group_billing_fields(request):
    if request.GET.get('group_billing'):
        return HttpResponse('')
    else:
        form = BillingCaseForm()
        return render(request, 'gbsapp/form_sections/group_billing.html', {'form': form})

def e_invoice_address(request):
    form = BillingCaseForm()
    return render(request,'gbsapp/form_sections/einvoice_address.html',{'form':form})

## pdf-laskun tekeminen ja tallentaminen tietokantaan:
def make_pdf_invoice(billing_case_id: int):
    try:
        inv_case = BillingCase.objects.get(id=billing_case_id)
        # haetaan laskutusasiakkaan tiedot:
        billing_cust = inv_case.billing_cust_id
        p_name = billing_cust.company_name
        p_address = billing_cust.address
        p_zip = billing_cust.postcode
        p_city = billing_cust.postoffice
        p_country = ''
        p_business_id = billing_cust.company_id
        i_service = inv_case.job_date.strftime("%d.%m.%Y") + ", " + inv_case.work_task + ", " + inv_case.work_description + ", " + inv_case.job_location
        i_pcs = inv_case.number_of_members
        i_price = inv_case.payment
        i_vat_prec = inv_case.vat_percent
        i_vat_included = inv_case.vat_includes
        i_payer_reference = inv_case.payer_reference

    except BillingCase.DoesNotExist:
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

def customer_dashboard(request, userid):
    customer = request.GET.objects('customer', user_id=userid)
    return render(request, 'gbsapp/dashboards/customer.html', {'customer': customer})
