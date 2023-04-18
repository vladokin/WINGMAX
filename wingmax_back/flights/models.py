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
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=6, unique=True)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    tickets_total = models.IntegerField(default=0)
    tickets_left = models.IntegerField()

    def __str__(self):
        return self.flight_number


#  Ticket model
class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.flight.flight_number + ' - ' + self.customer.user.username