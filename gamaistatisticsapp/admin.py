from django.contrib import admin
from .models import User,d45,Notes,moyenne,moyenneE

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','matricule','name','email','password','age','sexe')

admin.site.register(d45)
 
admin.site.register(moyenne) 
admin.site.register(moyenneE)   


@admin.register(Notes)    
class NotesAdmin(admin.ModelAdmin):
    list_display=('id','matricule','matiere1','matiere2','matiere3','matiere4','matiere5','matiere6')