from django.shortcuts import render
from gbsapp.models import BillingCase
from django.db.models import Sum, Q
from django.utils import timezone
from datetime import timedelta
from .forms import BillingCaseForm
from django.shortcuts import redirect
from .services.services import BillingCalculators
from django.http import HttpResponse

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
    else:
        lasku_form = BillingCaseForm()
    
    if lasku_form.is_valid():
        uusi_lasku = lasku_form.save(commit=False)
        uusi_lasku.stage = 'open'
       # uusi_lasku.frontman_cust_id = uusi_lasku.billing_cust_id
        uusi_lasku.owner_profit = BillingCalculators.calculate_customer_portion(
            uusi_lasku.payment,
            uusi_lasku.number_of_members or 1
        )
        uusi_lasku.save()
        return redirect('lasku_luotu', pk=uusi_lasku.pk)
    
    else:    
        return render(request, 'gbsapp/laskutus/lasku_new.html',{'form': lasku_form})

         
def lasku_luotu(request):
    return render(request, 'gbsapp/laskutus/lasku_new_confirm.html')
    

def lasku_detail(request, pk):
    invoice = BillingCase.objects.get(pk=pk)
    return render(request, 'gbsapp/laskutus/lasku_detail.html', {'invoice': invoice})

def group_billing_fields(request):
    if request.get('group_billing'):
        form = BillingCaseForm()
        return render(request, 'gbsapp/form_sections/group_billing.html', {'form': form})
    else:
        return HttpResponse('')

def e_invoice_address(request):
    form = BillingCaseForm()
    return render(request,'gbsapp/form_sections/einvoice_address.html',{'form':form})