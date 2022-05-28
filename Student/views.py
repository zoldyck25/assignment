from django.shortcuts import render, redirect
from form.models import register

def home(request):
    if request.method == 'POST':
        s1=eval(request.POST.get('physics_marks'))
        s2=eval(request.POST.get('chemistry_marks'))
        s3=eval(request.POST.get('cs_marks'))
        t=s1+s2+s3
        per=t*100/300
        data={
            't':t,
            'per':per
        }
        return render (request, 'home.html',data)

       
    details=register.objects.all()
    params={
        'details':details
    }  
    
    return render (request, 'home.html',params)
