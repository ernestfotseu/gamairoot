from django.forms import fields,widgets
from django.core import validators
from django import forms
from  .models import User,Notes

class enregisEtudiant(forms.ModelForm):
     class Meta:
        model = User
        fields=['matricule','name','email','password','age','sexe']
        widgets={
           'matricule': forms.TextInput(attrs={'class': 'form-control'}),
           'name': forms.TextInput(attrs={'class': 'form-control'}),
           'email': forms.EmailInput(attrs={'class': 'form-control'}),
           'password': forms.PasswordInput(render_value=True,attrs={'class': 'form-control'}),
           'age': forms.NumberInput(attrs={'class': 'form-control'}),
           'sexe': forms.TextInput(attrs={'class': 'form-control'}),
           
           
        }
        
        
class enregisNotes(forms.ModelForm):
   class Meta:
         model = Notes
         fields=['matricule','matiere1','matiere2','matiere3','matiere4','matiere5','matiere6']   
         widgets={
           'matricule': forms.TextInput(attrs={'class': 'form-control'}),
           'matiere1': forms.NumberInput(attrs={'class': 'form-control'}),
           'matiere2': forms.NumberInput(attrs={'class': 'form-control'}),
           'matiere3': forms.NumberInput(attrs={'class': 'form-control'}),
           'matiere4': forms.NumberInput(attrs={'class': 'form-control'}),
           'matiere5': forms.NumberInput(attrs={'class': 'form-control'}),
           'matiere6': forms.NumberInput(attrs={'class': 'form-control'}),
           
           
        }