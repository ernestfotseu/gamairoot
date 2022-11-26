from dataclasses import fields
import django_filters

from .models import User


class filtresU(django_filters.FilterSet):
    class Meta:
           model=User
           fields='__all__' 