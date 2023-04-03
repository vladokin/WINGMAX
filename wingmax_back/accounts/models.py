from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.forms import ValidationError


#  Custom User Manager
class UserManager (BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('email is required')
        if not username:
            raise ValueError('username is required')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        ) 
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        if User.objects.filter(is_superuser = True).exists():
            raise ValidationError('Only one superuser can be created')
        else:
            user = self.create_user(
                email = self.normalize_email(email),
                username = username,
                password = password,
            )
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user 


#  Custom User model
class User(AbstractBaseUser):
    #  Definition of the available user roles
    ADMIN = 1
    CUSTOMER = 2
    AIRLINE = 3
    
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CUSTOMER, 'Customer'),
        (AIRLINE, 'Airline')
    )
    
    #  Definition of the model fields
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=50, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,blank=True,null=True)
    
    #  Definition of Django required user model fields 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    #  Set email field as the username
    USERNAME_FIELD = 'email'
    
    #  Set username field as required
    REQUIRED_FIELDS = ['username']
    
    #  Connect UserManager to the User model
    objects = UserManager()
    
    #  Definition of some methods
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    
    def get_role(self):
        if self.role == 1:
            return 'Admin'
        elif self.role == 2:
            return 'Customer'
        elif self.role == 3:
            return 'Airline'