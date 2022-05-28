from django.shortcuts import render, redirect
from form.models import register

def home(request):       
    details=register.objects.all()
    params={
        'details':details
    }  
    
    return render (request, 'home.html',params)
