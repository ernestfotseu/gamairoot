from django.contrib import admin
import os,sys
sys.path.append('./models')
from users.models import User


# Register your models here.
admin.site.register(User)
