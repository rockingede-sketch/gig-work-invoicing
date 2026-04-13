from django.shortcuts import render
from gbsapp.models import BillingCase
from django.db.models import Sum, Q
from django.utils import timezone
from datetime import timedelta
from .forms import BillingCaseForm

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
        # POST — what do we pass to the template?
        # 1. take the submitted data and pass it to the form
        # 2. check if it's valid
        '''
        e_invoice_address is only required if verkkolasku is 1. Verkkolasku is required

group_name, number_of_members required only if group_billing is 1 and always required
let's do searchable combo box dropdown perhaps for now, pull customers from the model
        
        # 3. if valid — we manually set to open, retrieve the owner profit and caluclate the profit for the lasku - this should be done as an application available function. billing cust id can come from the logged in customer (which is not done right now, so this needs to be handled somehow).
        # 4. Yes we could redirect to created template / view def.
        pass
    else:
        billing_cust_id = forms.ModelChoiceField(queryset=Customer.objects.all())
        pass
        job location
        a date
        job started, job ended, work description, work_task, contact details
        billing method is selected
        e_invoice address if it is a verkkolasku
        paying reference
        the payment
        group billingy yes/no then group name
        number of members
        VAT included and at what percent.
        # GET — what do we pass to the template?
         '''
    return render(request, 'gbsapp/laskutus/lasku_new.html')

         
def lasku_luotu(request):
    return render(request, 'gbsapp/laskutus/lasku_new_confirm.html')
    

def lasku_detail(request, pk):
    invoice = BillingCase.objects.get(pk=pk)
    return render(request, 'gbsapp/laskutus/lasku_detail.html', {'invoice': invoice})