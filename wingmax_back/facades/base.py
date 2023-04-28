from abc import ABC
from flights.models import Flight
from accounts.models import Airline,User
from .utils import send_verification_email, activate_user, send_password_reset_email, password_reset_decoder


#  Definition of the BaseFacade class
class BaseFacade(ABC):
    def get_all_flights(self):
        '''Returns all the flights.'''
        return Flight.objects.all()
    
    def get_flight_by_id(self, flight_id):
        '''Returns a flight by its id.'''
        try:
            return Flight.objects.get(id=flight_id) 
        except Flight.DoesNotExist:
            return None
    
    def get_flight_by_route(self, departure_airport, arrival_airport):
        '''Returns a flight by its route.'''
        try:
            return Flight.objects.get(departure_airport=departure_airport, arrival_airport=arrival_airport)
        except Flight.DoesNotExist:
            return None
    
    def get_all_airlines(self):
        '''Returns all the airlines.'''
        return Airline.objects.all()
    
    def get_airline_by_id(self, airline_id):
        '''Returns an airline by its id.'''
        try:
            return Airline.objects.get(id=airline_id)
        except Airline.DoesNotExist:
            return None
    
    def get_airline_by_name(self, airline_name):
        '''Returns an airline by its name.'''
        try:
            return Airline.objects.get(name=airline_name)
        except Airline.DoesNotExist:
            return None
    
    def create_user(self, request):
        '''Creates a new user.'''
        try:
            data = request.data
            password = data['password1'] if data['password1'] == data['password2'] else None
            user = User.objects.create(email=data['email'], username=data['username'])
            user.set_password(password)
            user.save()
            send_verification_email(request, user)
            return user
        except Exception as e:
            return None
        
    def activate_user(self, uidb64, token):
        '''Activates a user account.'''
        return activate_user(uidb64, token)

    def forgot_password(self, request, email):
        '''Sends a password reset email to the user.'''
        try:
            user = User.objects.get(email=email)
            email_subject = 'Reset your password'
            email_template = 'emails/account_password_reset_email.html'
            send_password_reset_email(request, user, email_subject, email_template)
            return True
        except User.DoesNotExist:
            return False
    
    def reset_password(self, user, password1, password2):
        '''Resets a user password.'''
        try:
            password = password1 if password1 == password2 else None
            user.set_password(password)
            user.save()
            return True
        except Exception as e:
            return False