from .base import BaseFacade
from accounts.models import Airline
from flights.models import Flight


class AirlineFacade(BaseFacade):
    def update_airline(self, airline_id, airline_logo, name, country, phone_number):
        '''Updates an airline profile.'''
        try:
            airline = Airline.objects.get(pk=airline_id)
            airline.airline_logo = airline_logo
            airline.name = name
            airline.country = country
            airline.phone_number = phone_number
            airline.save()
            return airline
        except Airline.DoesNotExist:
            return None
    
    def add_flight(self, airline_id, departure_airport, arrival_airport, departure_date, arrival_date, price, tickets):
        '''Adds a flight to an airline profile.'''
        try:
            airline = Airline.objects.get(pk=airline_id)
            flight = Flight.objects.create(airline=airline, departure_airport=departure_airport, arrival_airport=arrival_airport, departure_date=departure_date, arrival_date=arrival_date, price=price, tickets_total=tickets, tickets_left=tickets)
            return flight
        except Airline.DoesNotExist:
            return None
    
    def update_flight(self, flight_id, departure_airport, arrival_airport, departure_date, arrival_date, price, tickets_max, tickets_left):
        '''Updates a flight.'''
        try:
            flight = Flight.objects.get(pk=flight_id)
            flight.departure_airport = departure_airport
            flight.arrival_airport = arrival_airport
            flight.departure_date = departure_date
            flight.arrival_date = arrival_date
            flight.price = price
            flight.tickets_total = tickets_max
            flight.tickets_left = tickets_left
            flight.save()
            return flight
        except Flight.DoesNotExist:
            return None
    
    def delete_flight(self, flight_id):
        '''Deletes a flight.'''
        try:
            flight = Flight.objects.get(pk=flight_id)
            flight.delete()
            return True
        except Flight.DoesNotExist:
            return False
    
    def get_all_flights(self, airline):
        '''Returns all the flights of an airline.'''
        return super().get_flights_by_airline(airline)
