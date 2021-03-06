from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


# Create your models here.
class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None,  **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
class CustomUser(AbstractUser):
    username = models.CharField(_('Username'),max_length=50,blank=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=12,unique=True, blank=True)
    is_student = models.BooleanField(default= False)
    is_teacher = models.BooleanField(default= False)
    is_admin = models.BooleanField(default = False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    standard = models.IntegerField()
    add = models.CharField(max_length=255)
    
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    subject = models.CharField(max_length=255)
    add = models.CharField(max_length=255)
    

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    add = models.CharField(max_length=255)
    
    
    
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/useremail/<filename>
    return 'media/{0}/{1}'.format(instance.user, filename)
         
class Image(models.Model):
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name='user')
    photo = models.ImageField(upload_to=user_directory_path)
    date = models.DateTimeField(auto_now_add=True)            