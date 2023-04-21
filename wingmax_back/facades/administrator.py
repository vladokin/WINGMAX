from .base import BaseFacade
from .utils import password_generator, send_password_email
from accounts.models import Customer, Airline, Administrator


class AdministratorFacade(BaseFacade):
    def create_customer(self, request, first_name, last_name, email, username):
        '''Creates a new customer.'''
        try:
            password1 = password2 = password_generator()
            user = super.create_user(request, email, username, password1, password2)
            user.role = 'Customer'
            customer = Customer.objects.create(user=user, first_name=first_name, last_name=last_name)
            email_subject = 'A user has created for you'
            email_template = 'emails/account_password_email.html'
            send_password_email(request, user, email_subject, email_template)
            return customer
        except Exception as e:
            return None

    def create_airline(self, request, name, iata_code, email, username):
        '''Creates a new airline.'''
        try:
            password1 = password2 = password_generator()
            user = super.create_user(request, email, username, password1, password2)
            user.role = 'Airline'
            airline = Airline.objects.create(user=user, name=name, iata_code=iata_code)
            email_subject = 'A user has created for you'
            email_template = 'emails/account_pass_email.html'
            send_password_email(request, user, email_subject, email_template)
            return airline
        except Exception as e:
            return None

    def create_administrator(self, request, first_name, last_name, email, username):
        '''Creates a new administrator.'''
        try:
            password1 = password2 = password_generator()
            user = super.create_user(request, email, username, password1, password2)
            user.role = 'Administrator'
            administrator = Administrator.objects.create(user=user, first_name=first_name, last_name=last_name)
            email_subject = 'A user has created for you'
            email_template = 'emails/account_pass_email.html'
            send_password_email(request, user, email_subject, email_template)
            return administrator
        except Exception as e:
            return None

    def get_all_customers(self):
        '''Returns all the customers.'''
        try:
            return Customer.objects.all()
        except Customer.DoesNotExist:
            return None

    def get_all_airlines(self):
        '''Returns all the airlines.'''
        try:
            return Airline.objects.all()
        except Airline.DoesNotExist:
            return None

    def get_all_administrators(self):
        '''Returns all the administrators.'''
        try:
            return Administrator.objects.all()
        except Administrator.DoesNotExist:
            return None

    def delete_customer(self, customer_id):
        '''Deletes a customer.'''
        try:
            customer = Customer.objects.get(pk=customer_id)
            user = customer.user
            user.delete()
            return True
        except Customer.DoesNotExist:
            return False

    def delete_airline(self, airline_id):
        '''Deletes an airline.'''
        try:
            airline = Airline.objects.get(pk=airline_id)
            user = airline.user
            user.delete()
            return True
        except Airline.DoesNotExist:
            return False

    def delete_administrator(self, administrator_id):
        '''Deletes an administrator.'''
        try:
            administrator = Administrator.objects.get(pk=administrator_id)
            user = administrator.user
            user.delete()
            return True
        except Administrator.DoesNotExist:
            return False