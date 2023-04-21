from django.contrib.auth import authenticate
from .base import BaseFacade
from accounts.models import Customer, Airline


class AnonymousFacade(BaseFacade):
    def login(self, email, password):
        '''Logs in a user.'''
        user = authenticate(email=email, password=password)
        if user is not None:
            return user
        else:
            return None

    def create_customer(self, request, first_name, last_name, email, username, password1, password2):
        '''Creates a new customer.'''
        try:
            user =  super.create_user(request, email, username, password1, password2)
            user.role = 'Customer'
            customer = Customer.objects.create(user=user, first_name=first_name, last_name=last_name)
            return customer
        except Exception as e:
            return None
    
    def create_airline(self, request, name, iata_code, email, username, password1, password2):
        '''Creates a new airline.'''
        try:
            user =  super.create_user(request, email, username, password1, password2)
            user.role = 'Airline'
            airline = Airline.objects.create(user=user, name=name, iata_code=iata_code)
            return airline
        except Exception as e:
            return None