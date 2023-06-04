from rest_framework.decorators import api_view
from rest_framework.response import Response
from facades.base import BaseFacade


@api_view(['GET'])
def get_all_flights():
    data = BaseFacade().get_all_flights()
    return Response(data)


@api_view(['GET'])
def get_flight_by_id(request, id):
    data = BaseFacade().get_flight_by_id(id)
    return Response(data)


@api_view(['POST'])
def get_flight_by_route(request, departure_airport, arrival_airport):
    data = BaseFacade().get_flight_by_route(departure_airport, arrival_airport)
    return Response(data)


