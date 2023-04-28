from django.core.exceptions import PermissionDenied


def user_is_administrator(user):
    '''Checks if the user is an administrator.'''
    return True if user.role == 1 else PermissionDenied


def user_is_customer(user):
    '''Checks if the user is a customer.'''
    return True if user.role == 2 else PermissionDenied


def user_is_airline(user):
    '''Checks if the user is an airline.'''
    return True if user.role == 3 else PermissionDenied