from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import jwt, accounts

app_name = 'api'

urlpatterns = [
    path('users/login/', jwt.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register_customer/', accounts.register_customer, name='register_customer'),
    path('users/activate/<uidb64>/<token>/', accounts.activate_user, name='activate_user'),
    path('users/register_airline/', accounts.register_airline, name='register_airline')
]
