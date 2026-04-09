from django.shortcuts import render
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from gbsapp.models import BillingCase
# Create your views here.
#class sendConfirmEmail(APIView):
   # def get(self, request):
   #     EmailService.sendConfirmEmail('test','email@email.com')
   #     
   #     return Response({'message': 'Welcome email sent'}, status=status.HTTP_200_OK)
 

def laskutus(request):
    invoices = BillingCase.objects.all()
    return render(request, 'gbsapp/laskutus/laskutus.html', {'invoices': invoices})

def lasku_new(request):
    return render(request, 'gbsapp/laskutus/lasku_new.html')

def lasku_detail(request, pk):
    invoice = BillingCase.objects.get(pk=pk)
    return render(request, 'gbsapp/laskutus/lasku_detail.html', {'invoice': invoice})