from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#class sendConfirmEmail(APIView):
   # def get(self, request):
   #     EmailService.sendConfirmEmail('test','email@email.com')
   #     
   #     return Response({'message': 'Welcome email sent'}, status=status.HTTP_200_OK)
 
def laskutus(request):
    return render(request, 'laskutus.html')