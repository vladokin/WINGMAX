from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import jwt, accounts, base

app_name = 'api'

urlpatterns = [
    path('users/login/', jwt.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register-customer/', accounts.register_customer, name='register_customer'),
    path('users/activate/<uidb64>/<token>/', accounts.activate_user, name='activate_user'),
    path('users/register-airline/', accounts.register_airline, name='register_airline'),
    path('users/forgot-password/', accounts.forgot_password, name='forgot_password'),
    path('users/reset-password/<uidb64>/<token>/', accounts.reset_password_auth, name='reset_password_auth'),
    path('users/reset-password/', accounts.reset_password, name='reset_password'),
    
    path('flights/', base.get_all_flights, name='get_all_flights'),
    path('flights/<int:id>/', base.get_flight_by_id, name='get_flight_by_id'),
    path('flights/<str:departure_airport>/<str:arrival_airport>/', base.get_flight_by_route, name='get_flight_by_route'),
    
]
