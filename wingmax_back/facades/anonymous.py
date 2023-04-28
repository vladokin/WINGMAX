from django.contrib.auth import authenticate
from .base import BaseFacade
from accounts.models import Customer, Airline, User


class AnonymousFacade(BaseFacade):
    def login(self, email, password):
        '''Logs in a user.'''
        user = authenticate(email=email, password=password)
        if user is not None:
            return user
        else:
            return None

    def create_customer(self, request):
        '''Creates a new customer.'''
        try:
            data = request.data
            user =  super().create_user(request)
            user.role = User.CUSTOMER
            user.save()
            customer = Customer.objects.create(user=user, first_name=data['first_name'], last_name=data['last_name'])
            customer.save()
            return customer
        except Exception as e:
            return None
    
    def create_airline(self, request):
        '''Creates a new airline.'''
        try:
            data = request.data
            user =  super().create_user(request)
            user.role = User.AIRLINE
            user.save()
            airline = Airline.objects.create(user=user,iata_code=data['iata_code'], name=data['name'])
            airline.save()
            return airline
        except Exception as e:
            return None
        