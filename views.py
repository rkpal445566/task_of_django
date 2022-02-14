from app_1.models import User
from app_1 .forms import Student
from django.shortcuts import render ,HttpResponseRedirect


# Create your views here.
def fun(request):
    if request.method == 'POST':
        RK=Student(request.POST)
        if RK.is_valid():
            nm=RK.cleaned_data['name']
            em=RK.cleaned_data['Email']
            pw=RK.cleaned_data['password']
            reg= User(name=nm, Email=em ,password=pw)
            reg.save()
            RK=Student()   
    else:
     RK=Student()    
    stud = User .objects.all()
    return render(request,'app_1/add_show.html', {'var1':RK, 'var2':stud})
    
    #this function will ubdate/addit


def ubdate_data(request,id):
    if request.method =='POST':
         pi= User.objects.get(pk=id)
         fm=Student(request.POST, instance=pi)
         if fm.is_valid():
          fm.save()
    else:
      pi=User.objects.get(pk=id)
    fm=Student(instance = pi)    
    return render(request, 'app_1/ubdate.html',{'ubd':fm})
    
    
    
    
    #this function is delet
    
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm=Student(request.POST, instance=pi)
        if fm.is_valid():
          fm.save()
   
        fm=Student()
    return render(request,'app_1/ubdate.html',{'ubd':fm}) 