from ..serializers import CustomerSerializer, AirlineSerializer
from rest_framework.decorators import api_view
from facades.anonymous import AnonymousFacade
from facades.base import BaseFacade
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.response import Response
from facades.utils import password_reset_decoder


@api_view(['POST'])
def register_customer(request):
    '''Registers a new customer.'''
    try:
        customer = AnonymousFacade().create_customer(request)
        serializer = CustomerSerializer(customer, many=False)
        return Response( serializer.data )
    except Exception as e:
        return Response({'error': str(e)})


def activate_user(request, uidb64, token):
    '''Activates a user account.'''
    try:
        user = BaseFacade().activate_user(uidb64, token)
        if user is not None:
            redirect('http://localhost:5173/login')
            return JsonResponse({'message': 'Account activated successfully!'})
        else:
            redirect('http://localhost:5173')
            return JsonResponse({'error': 'Invalid activation link'})
    except Exception as e:
            redirect('http://localhost:5173')
            return JsonResponse({'error': str(e)})


@ api_view(['POST'])
def register_airline(request):
    '''Registers a new airline.'''
    try:
        airline = AnonymousFacade().create_airline(request)
        serializer = AirlineSerializer(airline, many=False)
        return Response( serializer.data )
    except Exception as e:
        return Response({'error': str(e)})


@ api_view(['POST'])
def forgot_password(request):
    '''Sends a password reset email.'''
    try:
        BaseFacade().forgot_password(request)
        redirect('http://localhost:5173')
        return JsonResponse({'message': 'Password reset email sent!'})
    except Exception as e:
        redirect('http://localhost:5173')
        return JsonResponse({'error': str(e)})



def reset_password_auth(request, uidb64, token):
    '''Authenticates a password reset request.'''
    user =  password_reset_decoder(uidb64, token)
    if user is not None:
        redirect('http://localhost:5173/reset-password')
        return JsonResponse({'message': 'Password reset link is valid!', 'user': user})
    else:
        redirect('http://localhost:5173')
        return JsonResponse({'error': 'Invalid password reset link!', 'user': None})


@api_view(['POST'])
def reset_password(request):
    '''Resets a user's password.'''
    try:
        user = BaseFacade().reset_password(request)
        redirect('http://localhost:5173/login')
        return JsonResponse({'message': 'Password reset successfully!'})
    except Exception as e:
        redirect('http://localhost:5173')
        return JsonResponse({'error': str(e)})