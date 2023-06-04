from django.db import models
from accounts.models import Customer, Airline


#  Airport model
class Airport(models.Model):
    name = models.CharField(max_length=50)
    iata_code = models.CharField(max_length=3, unique=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


#  Flight model
class Flight(models.Model):
    
    #  Definition of available flight status choices
    PLANNED = 1
    TAKING_OFF = 2
    ON_ROUTE = 3
    LANDING = 4
    COMPLETED = 5
    CANCELED = 6
    MAXED_OUT = 7
    
    STATUS_CHOICES = (
        (PLANNED, 'Planned'),
        (TAKING_OFF, 'Taking off'),
        (ON_ROUTE, 'On route'),
        (LANDING, 'Landing'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
        (MAXED_OUT, 'Maxed out')
    )
    
    # Definition of the model field
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=6, unique=True)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    tickets_total = models.IntegerField(default=0)
    tickets_left = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=PLANNED)

    def __str__(self):
        return self.flight_number
    
    def get_status(self):
        '''Returns the flight status as a string.'''
        return {
            1: 'Planned',
            2: 'Taking off',
            3: 'On route',
            4: 'Landing',
            5: 'Completed',
            6: 'Canceled',
            7: 'Maxed out'
        }.get(self.status)


#  Ticket model
class Ticket(models.Model):
    #  Definition of available ticket status choices
    ACTIVE = 1
    CANCELED = 2
    COMPLETED = 3
    
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (CANCELED, 'Canceled'),
        (COMPLETED, 'Completed'),
    )
    
    #  Definition of the model field
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.flight.flight_number + ' - ' + self.customer.user.username
    
    def get_status(self):
        '''Returns the ticket status as a string.'''
        return {
            1: 'Active',
            2: 'Canceled',
            3: 'Completed',
        }.get(self.status)