from django.contrib import admin
from .models import User, Customer, Airline, Administrator


#  Registering the accounts app models
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Airline)
admin.site.register(Administrator)
