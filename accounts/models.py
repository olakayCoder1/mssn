from datetime import datetime
from statistics import mode
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, first_name, password, **other_fields)


    def create_user(self, email, first_name,password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user



def upload_to(instance, filename):
    return 'profile/{filename}'.format(filename=filename)





class CustomUser(AbstractBaseUser, PermissionsMixin):
    AUTH_PROVIDERS = (
        ('email','email'),
        ('google','google')
    )
    public_id = models.CharField(max_length=10 , null=True , blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=100, null=True , blank=True )
    last_name = models.CharField(max_length=100, null=True , blank=True )
    phone = models.CharField(max_length=20 , null=True , blank=True ) 
    image = models.ImageField(upload_to=upload_to , default='profiles/image-default.png', null=True , blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    auth_provider = models.CharField(max_length=10, choices=AUTH_PROVIDERS , default='email')
    updated_at = models.DateTimeField(auto_now=True) 
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email




class CommitteePosition(models.Model):
    public_id = models.CharField(max_length=10 , null=True , blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Committee(models.Model):
    USER_GENDER = (
        ('male','male'),
        ('female','female')
    )
    public_id = models.CharField(max_length=10 , null=True , blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.ForeignKey(
        CommitteePosition , 
        on_delete=models.CASCADE,
        help_text=_("The post of this committee has") 
    )
    gender = models.CharField(
        max_length=10,
        choices=USER_GENDER,
        null=True, blank=True ,
    )
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class TokenActivation(models.Model):
    public_id = models.CharField(max_length=10 , null=True , blank=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

