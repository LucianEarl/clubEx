from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

"""
---------------------------------------------------------------------------------------------------------------------------------------------
django.db is the database that's been imported elsewhere.
---------------------------------------------------------------------------------------------------------------------------------------------
"""

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, physical_address, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have an last name")
        if not physical_address:
            raise ValueError("Users must have a address")
        if not phone_number:
            raise ValueError("Users must have a phone number")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            physical_address=physical_address,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name, last_name, physical_address, phone_number):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            physical_address=physical_address,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

"""
---------------------------------------------------------------------------------------------------------------------------------------------
create_user is an object that is being defined to call a function for each arguement
by displaying an error if the input is incorrect.

user = self.model is being used as an instance of a class by using the self keyword by accessing
attributes and methods within it's own model. The model has it's own parameters and if true
for each user, a return statement is used to end the execution of a function.

also applies to the create_superuser.
---------------------------------------------------------------------------------------------------------------------------------------------
"""


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, unique=False)
    last_name = models.CharField(max_length=30, unique=False)
    physical_address = models.CharField(max_length=300, unique=False)
    phone_number = models.CharField(max_length=10)
    subscription_plan = models.CharField(max_length=10, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'physical_address',
        'phone_number'
    ]

    objects = MyAccountManager()

    def __str__(self):
        return self.pk


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

"""
---------------------------------------------------------------------------------------------------------------------------------------------
An object called Account(AbstractBaseUser) is being called to use an abstract method
---------------------------------------------------------------------------------------------------------------------------------------------
"""