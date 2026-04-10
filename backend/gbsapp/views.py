from django.shortcuts import render
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from gbsapp.models import BillingCase
from django.db.models import Sum, Q
from django.utils import timezone
# Create your views here.
#class sendConfirmEmail(APIView):
   # def get(self, request):
   #     EmailService.sendConfirmEmail('test','email@email.com')
   #     
   #     return Response({'message': 'Welcome email sent'}, status=status.HTTP_200_OK)
 

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
    late_invoices = invoices.filter(is_late=True,stage__in=['invoice sent'])
    late_count = late_invoices.count()
    late_total = late_invoices.aggregate(t=Sum('payment'))['t'] or 0

    #Paid invoices
    paid_invoices = invoices.filter(stage='invoice paid')
    paid_count = paid_invoices.count()
    paid_total = paid_invoices.aggregate(t=Sum('payment'))['t'] or 0
    
    if filter_status == 'open':
        invoices = open_invoices
    elif filter_status == 'paid':
        invoices = paid_invoices

    context = {
        'invoices': invoices,
        'status_filter': filter_status,
        'total_count': invoice_total_count,
        'open_count': open_count,
        'late_count': late_count,
        'late_total': late_total,
        'paid_count': paid_count,
        'open_total': open_total,
        'paid_total': paid_total,
    }

    return render(request, 'gbsapp/laskutus/laskutus.html', {'invoices': invoices})

def lasku_new(request):
    return render(request, 'gbsapp/laskutus/lasku_new.html')

def lasku_detail(request, pk):
    invoice = BillingCase.objects.get(pk=pk)
    return render(request, 'gbsapp/laskutus/lasku_detail.html', {'invoice': invoice})