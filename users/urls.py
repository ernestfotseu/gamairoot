from django.urls import path
from users.views import home,register,personnels,etudiants,admins



urlpatterns = [
    path('',home,name='home'),
    path('register', register,name='register'),
    path('personnels',personnels,name='personnels'),
    path('etudiants',etudiants,name='etudiants'),
    path('admins',admins,name='admins'),
]
