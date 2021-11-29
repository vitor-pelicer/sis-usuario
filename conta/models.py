from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    nome = models.CharField(max_length = 255)
    username = models.CharField(max_length=150, unique=True, blank=False, null=False, default="")
    nascimento = models.DateField()
    password = models.CharField(max_length=128, blank=False, null=False, default="")
