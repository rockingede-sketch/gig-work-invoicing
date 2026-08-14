from urllib import request

from django.apps import apps
from django.http import HttpResponse
from gbsapp.models import Customer
# Palauttaa asiakkaan nimen ja id:n, jos request on validi ja käyttäjä on kirjautunut sisään. Muuten palauttaa tyhjän nimen ja None id:n.
class Asiakas:
    @staticmethod
    def get_customer_info(request):
    # Tarkista onko request tai user olemassa ennen käyttöä
        if request is None or not hasattr(request, 'user') or request.user.is_anonymous:
            return {'customer_name': '', 'customer_id': None}
        
        try:
            customer = Customer.objects.get(user_id=request.user.id)
            return {
                'customer_name': f"{customer.first_name} {customer.last_name}",
                'customer_id': Customer.objects.get(user_id=request.user.id).id, # type: ignore
            }
        except Customer.DoesNotExist:
            return {'customer_name': 'Tuntematon asiakas', 'customer_id': None}
    
   