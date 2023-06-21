from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .form import RegistrationForm
from django.http import HttpResponseRedirect
def signup(request):
    if request.method=='POST':
        
        form=RegistrationForm(request.POST)
       
        if form.is_valid():
            
             
             form.save()
             U=form.cleaned_data['username']
             return render(request,'dashboard.html' ,{'username':U})
    else:
        form=RegistrationForm()
    return render(request,'home.html' ,{'form':form})


def login(request):
     return render(request,'dashboard.html',{'username':request.user})
    