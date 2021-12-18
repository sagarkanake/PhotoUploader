# About The Project

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Logic">Logic</a></li>
    <li><a href="#Code">Code</a></li>
    <li><a href="#contributing">Installation</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
  </details>
  
# Built With
 *  Languages Used : Python , javascript , Html , CSs .
 *  Framework Used : Python Django Framework .
# Getting Started 
Simple task i.e a project with user register + Login . Register page has name, phone_number, email(unique=True) .Created a welcome page showing name of respective logged in user.

# Logic 
I have modified the Django user model. The modification involves phone field and email having a unique constraint . I Used a customized User model  to store phone_number and assign unique key constraint to email id . Beacuase default User model is not have the phone_number field and also we can't logged in the user through email id .
With the help of this CustomUser model Authentication of user is  performed through email id . 
# Code
## Custom User Model
Used to authenticate User with emal id and and eamil id have been unique key constraint 
* accounts/models.py
```python

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
```
## The Messages Framework
Used the messages framework to display a one-time notification message (also known as “flash message”) to the user after processing a form or some other types of user input.

# Packages
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 
# Installation
django = "*"

pillow = "*"

```bash
pipenv install Django
pipenv install Pillow


#Usage

```python
#Firstly created a virtual environment using 
pip install pipenv

#To create virtual Environment
pipenv shell env

#To activate the virtual Environment 
pipenv shell

# To start the project 
django-admin startproject project_name


#To Create app in django
pip install python manage.py startapp app_name


#To Run the server
python manage.py runserver


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
