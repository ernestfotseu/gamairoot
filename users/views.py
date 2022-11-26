from distutils.log import error
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

from users.form import UserForms
# Create your views here.
def home(request):
    error=""
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_admins:
                return redirect("admins")
            elif user.is_enseignants:
                return redirect('enseignants')
            elif user.is_personnels:
                return redirect('personnels')
            else:
                return redirect('etudiants')
        else:
            error='mot de passe ou nom utilisateur incorrect'    
    else:
            return render(request,'login.html',{'error':error})
        
        
        
def register(request):
    form=UserForms
    if request.method=='POST':
        form=UserForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'register.html',{'form':form})            


def admins(request):
    return render(request, 'etudiant/base2.html', {})
    #return render(request,'admins.html') 


def enseignants(request):
    return render (request,'enseignants.html')

def personnels(request):
    return render(request,'personnels.html')

def etudiants(request):
    return render(request,'etudiants.html') 


