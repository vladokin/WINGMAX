import random
import string 
from base64 import urlsafe_b64decode
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from accounts.models import User
from django.conf import settings


def send_verification_email(request,user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    subject = 'Thank you for registering to our site'
    message =   render_to_string('accounts/verification_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': uid,
        'token': token,
    })
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [str(user.email),]
    
    send_mail( subject, '', email_from, recipient_list, html_message=message, fail_silently=False )
    return ()
    
def activate_user(uidb64, token):
    '''Activates a user account.'''
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return user
    else:
        return None


def password_generator(size=8, chars=string.ascii_uppercase + string.digits):
    '''Generates a random password.'''
    return ''.join(random.choice(chars) for _ in range(size))


def send_password_email(request, user, email_subject, email_template):
    '''Sends an email to the user with his password.'''
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    massage = render_to_string(email_template, {
        'user': user,
        'domain': current_site.domain,
        'password': user.password,
    })
    to_email = user.email
    mail = EmailMessage(email_subject, massage, from_email, to=[to_email])
    mail.send()


def send_password_reset_email(request, user):
    '''Sends an email to the user with a link to reset his password.'''
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    subject = 'Password Reset'
    message =   render_to_string('accounts/account_password_reset_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': uid,
        'token': token,
    })
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [str(user.email),]
    
    send_mail( subject, '', email_from, recipient_list, html_message=message, fail_silently=False )
    return ()


def password_reset_decoder(uidb64, token):
    '''Decodes the uidb64 and token for password reset.'''
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        return user
    else:
        return None    
