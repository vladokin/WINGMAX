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
            user.is_active = True
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user 


#  Custom User model
class User(AbstractBaseUser):
    #  Definition of the available user roles
    ADMINISTRATOR = 1
    CUSTOMER = 2
    AIRLINE = 3
    
    ROLE_CHOICES = (
        (ADMINISTRATOR, 'Administrator'),
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
        '''Returns the role of the user as a string'''
        return {
            1: 'Administrator',
            2: 'Customer',
            3: 'Airline',
        }.get(self.role)

    def save(self, *args, **kwargs):
        '''Prevent the user role from being changed'''
        if self.pk:
            original = User.objects.get(pk=self.pk)
            if original.role != self.role:
                raise ValueError('User role cannot be changed')
        super().save(*args, **kwargs)


#  Customer model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_photo = models.ImageField(upload_to='accounts/profile_photos', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50,unique=True, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    zip_code = models.CharField(max_length=50,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    #  Set first_name and last_name fields as required
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def __str__(self):
        return self.user.username    


#  Airline model
class Airline(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    airline_logo = models.ImageField(upload_to='accounts/airline_logos', blank=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    iata_code = models.CharField(max_length=2, unique=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    phone_number = models.CharField(max_length=50,unique=True, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    #  Set name and iata_code fields as required
    REQUIRED_FIELDS = ['name','iata_code']
    
    def __str__(self):
        return self.user.username


#  Administrator model
class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_photo = models.ImageField(upload_to='accounts/profile_photos', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50,unique=True, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    #  Set first_name and last_name fields as required
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def __str__(self):
        return self.user.username