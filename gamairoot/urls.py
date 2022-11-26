"""projet_Uds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from django.views import View
from gamaistatisticsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('etudiant/',views.home1,name="home1"),
    path('delete/<int:id>/',views.delete_data,name="deletedata"),
    path('',include('users.urls')),
    
    path('statistique/',views.statistique,name='statistique'),
    path('statistique1/',views.statistique1,name='statistique1'),
    path('stat3/',views.stat3,name='stat3'),
    path('stat4/',views.stat4,name='stat4'),
    path('stat5/',views.stat5,name='stat5'),
    path('stat6/',views.stat6,name='stat6'),
    path('stat7/',views.stat7,name='stat7'),
    path('stat8/',views.stat8,name='stat8'),
    path('moyenne/',views.moyenne1,name='moyenne'),
    path('delete1/<int:id>/',views.delete_note,name="deletenote"),
    
    path('<int:id>/',views.update_note,name="updatenote"),
    path('<int:id>/',views.update_data,name="updatedata"),
]
