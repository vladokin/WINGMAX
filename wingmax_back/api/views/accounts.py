from ..serializers import CustomerSerializer, AirlineSerializer
from rest_framework.decorators import api_view
from facades.anonymous import AnonymousFacade
from facades.base import BaseFacade
from django.http import JsonResponse
from rest_framework.response import Response


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
            return JsonResponse({'message': 'Account activated successfully!'})
        else:
            return JsonResponse({'error': 'Invalid activation link'})
    except Exception as e:
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

