from django.shortcuts import render,redirect
from form.models import register
# Create your views here.

def form(request):
    if request.method == 'POST':
        student_name=request.POST['student_name']
        dob=request.POST['dob']
        s1=eval(request.POST.get('physics_marks'))
        s2=eval(request.POST.get('chemistry_marks'))
        s3=eval(request.POST.get('cs_marks'))
        t=s1+s2+s3
        per=t*100/300
        forms=register.objects.create(per=per,physics_marks=s1,chemistry_marks=s2,cs_marks=s3,student_name=student_name,dob=dob)

        forms.save()
        return redirect('home') 
  
    return render (request,"form.html") 
 