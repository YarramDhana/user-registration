from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def registration (request):
    EUFO=Userforms()
    EPFO=profileforms()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=='POST' and request.FILES:
        UFD=Userforms(request.POST)
        PFD=profileforms(request.POST,request.FILES )
        if UFD.is_valid() and PFD.is_valid:
            MUFD=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            MUFD.set_password(password)
            MUFD.save()


            PFD=PFD.save(commit=False)
            PFD.name=MUFD
            PFD.save()
            send_mail('registration','registration is successfully','yarramdhana369@gmail.com',[MUFD.email],fail_silently=False)


            return HttpResponse(' registration is successfully')


    return render (request,'registration.html',d)
    

