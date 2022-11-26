import email
from multiprocessing import context
from unicodedata import name
from django import views
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import enregisEtudiant, enregisNotes
from .models import Notes, User
from .models import d45,moyenne,moyenneE

# Create your views here.
def home1 (request):
    if request.method=='POST':
        fm=enregisEtudiant(request.POST)
        if fm.is_valid():
            mat=fm.cleaned_data['matricule']
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            ag=fm.cleaned_data['age']
            sx=fm.cleaned_data['sexe']
            reg=User(matricule=mat,name=nm,email=em,password=ps,age=ag,sexe=sx)
            reg.save()
            fm=enregisEtudiant()
    else:
        fm=enregisEtudiant()
    stud=User.objects.all()
    return render(request,'etudiant/base2.html',{'form':fm,'stu':stud})

def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=enregisEtudiant(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else :
        pi=User.objects.get(pk=id)
        fm=enregisEtudiant(instance=pi)        
        
    return render(request,"etudiant/modifier.html",{'form':fm})



def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/etudiant")
    
    
def statistique(request):
    no=User.objects.filter(age__gte=15).filter(age__lte=17).count()
    n1=User.objects.filter(age__gte=18).filter(age__lte=20).count()
    n2=User.objects.filter(age__gte=21).filter(age__lte=23).count()
    n3=User.objects.filter(age__gte=24).filter(age__lte=26).count()
    n4=User.objects.filter(age__gte=27).filter(age__lte=29).count()
    n5=User.objects.filter(age__gte=30).filter(age__lte=32).count()
    n6=User.objects.filter(age__gte=33).filter(age__lte=35).count()
    n7=User.objects.filter(age__gte=36).filter(age__lte=38).count()
    n8=User.objects.filter(age__gte=39).count()
    n9=User.objects.filter(age__gte=14).count()

    return render(request,'statistique/stat1.html',{'no':no,'n1':n1,'n2':n2,'n3':n3,'n4':n4,'n5':n5,'n6':n6,'n7':n7,'n8':n8,'n9':n9})


def statistique1(request):
    
    if request.method=='POST':
        fm=enregisNotes(request.POST)
        if fm.is_valid():
            mat=fm.cleaned_data['matricule']
            m1=fm.cleaned_data['matiere1']
            m2=fm.cleaned_data['matiere2']
            m3=fm.cleaned_data['matiere3']
            m4=fm.cleaned_data['matiere4']
            m5=fm.cleaned_data['matiere5']
            m6=fm.cleaned_data['matiere6']
            reg=Notes(matricule=mat,matiere1=m1,matiere2=m2,matiere3=m3,matiere4=m4,matiere5=m5,matiere6=m6)
            reg.save()
            fm=enregisNotes()
    else:
      fm=enregisNotes()
    nb=Notes.objects.all()  
    return render(request,'statistique/stat2.html',{'form':fm,'nb1':nb})
 
 
 
 
def delete_note(request,id):
        if request.method=='POST':
          pi=Notes.objects.get(pk=id)
          pi.delete()
          return HttpResponseRedirect("/statistique1")
      


def update_note(request,id):
    
    if request.method=='POST':
        pi=Notes.objects.get(pk=id)
        fm=enregisNotes(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else :
        pi=Notes.objects.get(pk=id)
        fm=enregisNotes(instance=pi)     
    
    return render(request,'statistique/mod1.html',{'form':fm})




def stat3(request):
    
    no=Notes.objects.exclude(matiere1__gt=9).count()
    no1=Notes.objects.filter(matiere1__gte=10).filter(matiere1__lte=11).count()
    no2=Notes.objects.filter(matiere1__gte=12).filter(matiere1__lte=13).count()
    no3=Notes.objects.filter(matiere1__gte=14).filter(matiere1__lte=15).count()
    no4=Notes.objects.filter(matiere1__gte=16).filter(matiere1__lte=17).count()
    no5=Notes.objects.filter(matiere1__gte=18).filter(matiere1__lte=20).count()
    no6=Notes.objects.filter(matiere1__lte=20).count()
    
    return render(request,'statistique/stat3.html',{'no':no,'no1':no1,'no2':no2,'no3':no3,'no4':no4,'no5':no5,'no6':no6})


def stat4(request):
    no=Notes.objects.exclude(matiere2__gt=9).count()
    no1=Notes.objects.filter(matiere2__gte=10).filter(matiere1__lte=11).count()
    no2=Notes.objects.filter(matiere2__gte=12).filter(matiere1__lte=13).count()
    no3=Notes.objects.filter(matiere2__gte=14).filter(matiere1__lte=15).count()
    no4=Notes.objects.filter(matiere2__gte=16).filter(matiere1__lte=17).count()
    no5=Notes.objects.filter(matiere2__gte=18).filter(matiere1__lte=20).count()
    no6=Notes.objects.filter(matiere2__lte=20).count()
    return render(request,'statistique/stat4.html',{'no':no,'no1':no1,'no2':no2,'no3':no3,'no4':no4,'no5':no5,'no6':no6})



def stat5(request):
    no=Notes.objects.exclude(matiere3__gt=9).count()
    no1=Notes.objects.filter(matiere3__gte=10).filter(matiere1__lte=11).count()
    no2=Notes.objects.filter(matiere3__gte=12).filter(matiere1__lte=13).count()
    no3=Notes.objects.filter(matiere3__gte=14).filter(matiere1__lte=15).count()
    no4=Notes.objects.filter(matiere3__gte=16).filter(matiere1__lte=17).count()
    no5=Notes.objects.filter(matiere3__gte=18).filter(matiere1__lte=20).count()
    no6=Notes.objects.filter(matiere3__lte=20).count()
    return render(request,'statistique/stat5.html',{'no':no,'no1':no1,'no2':no2,'no3':no3,'no4':no4,'no5':no5,'no6':no6})


def stat6(request):
    no=Notes.objects.exclude(matiere4__gt=9).count()
    no1=Notes.objects.filter(matiere4__gte=10).filter(matiere1__lte=11).count()
    no2=Notes.objects.filter(matiere4__gte=12).filter(matiere1__lte=13).count()
    no3=Notes.objects.filter(matiere4__gte=14).filter(matiere1__lte=15).count()
    no4=Notes.objects.filter(matiere4__gte=16).filter(matiere1__lte=17).count()
    no5=Notes.objects.filter(matiere4__gte=18).filter(matiere1__lte=20).count()
    no6=Notes.objects.filter(matiere4__lte=20).count()
    return render(request,'statistique/stat6.html',{'no':no,'no1':no1,'no2':no2,'no3':no3,'no4':no4,'no5':no5,'no6':no6})

def stat7(request):
    no=Notes.objects.exclude(matiere5__gt=9).count()
    no1=Notes.objects.filter(matiere5__gte=10).filter(matiere1__lte=11).count()
    no2=Notes.objects.filter(matiere5__gte=12).filter(matiere1__lte=13).count()
    no3=Notes.objects.filter(matiere5__gte=14).filter(matiere1__lte=15).count()
    no4=Notes.objects.filter(matiere5__gte=16).filter(matiere1__lte=17).count()
    no5=Notes.objects.filter(matiere5__gte=18).filter(matiere1__lte=20).count()
    no6=Notes.objects.filter(matiere5__lte=20).count()
    return render(request,'statistique/stat7.html',{'no':no,'no1':no1,'no2':no2,'no3':no3,'no4':no4,'no5':no5,'no6':no6})

def stat8(request):
    no=Notes.objects.exclude(matiere6__gt=9).count()
    no1=Notes.objects.filter(matiere6__gte=10).filter(matiere1__lte=11).count()
    no2=Notes.objects.filter(matiere6__gte=12).filter(matiere1__lte=13).count()
    no3=Notes.objects.filter(matiere6__gte=14).filter(matiere1__lte=15).count()
    no4=Notes.objects.filter(matiere6__gte=16).filter(matiere1__lte=17).count()
    no5=Notes.objects.filter(matiere6__gte=18).filter(matiere1__lte=20).count()
    no6=Notes.objects.filter(matiere6__lte=20).count()
    return render(request,'statistique/stat8.html',{'no':no,'no1':no1,'no2':no2,'no3':no3,'no4':no4,'no5':no5,'no6':no6})




def moyenne1(request):
    fm=moyenneE.objects.all()
    ef=moyenne.objects.all()
    
   
    return render (request,'statistique/moyenne.html',{'fm':fm,'ef':ef,'no':no})
