from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    matricule=models.CharField(max_length=200)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=71)
    password=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    sexe=models.CharField(max_length=50)
    
 
class d45(models.Model):
    category=models.CharField(max_length=100 , blank=False, null=False)
    effectif=models.PositiveIntegerField()
    
    
    def __str__(self):
        return f'{self.category}-{self.effectif}'
    
    
    
    
class Notes(models.Model):
    matricule=models.CharField(max_length=100)
    matiere1=models.PositiveIntegerField()
    matiere2=models.PositiveIntegerField()
    matiere3=models.PositiveIntegerField()
    matiere4=models.PositiveIntegerField()
    matiere5=models.PositiveIntegerField()
    matiere6=models.PositiveIntegerField()
    
    
    
class moyenne(models.Model):
    intervals=models.CharField(max_length=100 , blank=False, null=False)
    effectif=models.PositiveIntegerField()

    
    
    def __str__(self):
        return f'{self.intervals}-{self.effectif}'    
    
    
    
    
class moyenneE(models.Model):
    intervals=models.CharField(max_length=100 , blank=False, null=False)
    effectif=models.PositiveIntegerField()
    effectif1=models.PositiveIntegerField()
    effectif2=models.PositiveIntegerField()
    effectif3=models.PositiveIntegerField()
    effectif4=models.PositiveIntegerField()
    effectif5=models.PositiveIntegerField()
    
    
    def __str__(self):
        return f'{self.intervals}-{self.effectif}-{self.effectif1}-{self.effectif3}-{self.effectif4}-{self.effectif5}'        