from .base import BaseFacade
from accounts.models import Customer
from flights.models import Flight, Ticket


class CustomerFacade(BaseFacade):
    def ubdate_customer(self, customer_id, profile_photo, first_name, last_name, phone_number, address, state, country, city, zip_code):
        '''Updates a customer profile.'''
        try:
            customer = Customer.objects.get(pk=customer_id)
            customer.profile_photo = profile_photo
            customer.first_name = first_name
            customer.last_name = last_name
            customer.phone_number = phone_number
            customer.address = address
            customer.state = state
            customer.country = country
            customer.city = city
            customer.zip_code = zip_code
            customer.save()
            return customer
        except Customer.DoesNotExist:
            return None
        
    def add_ticket(self, customer_id, flight_id):
        '''Adds a ticket to a customer profile.'''
        try:
            customer = Customer.objects.get(pk=customer_id)
            flight = Flight.objects.get(pk=flight_id)
            ticket = Ticket.objects.create(customer=customer, flight=flight)
            return ticket
        except Customer.DoesNotExist:
            return None
    
    def get_all_tickets(self, customer_id):
        '''Returns all the tickets of a customer.'''
        try:
            customer = Customer.objects.get(pk=customer_id)
            return customer.tickets.all()
        except Customer.DoesNotExist:
            return None
    
    def delete_ticket(self, ticket_id):
        '''Deletes a ticket.'''
        try:
            ticket = Ticket.objects.get(pk=ticket_id)
            ticket.delete()
            return True
        except Ticket.DoesNotExist:
            return False