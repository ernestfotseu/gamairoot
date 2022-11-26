from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    is_admins = models.BooleanField(default=False)
    is_enseignants = models.BooleanField(default=False)
    is_personnels = models.BooleanField(default=False)
    is_etudiants = models.BooleanField(default=True)
