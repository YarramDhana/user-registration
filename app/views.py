from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


def registration (request):
    EUFO=Userforms()
    EPFO=profileforms()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=='POST' and request.FILES:
        UFD=Userforms(request.POST)
        PFD=profileforms(request.POST,request.FILES )
        if UFD.is_valid() and PFD.is_valid():
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
    

def home (request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render( request,'home.html',d)
    return render( request,'home.html')





def user_login (request):
    if request.method=="POST":
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))



    return render (request,'user_login.html')




@ login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@ login_required
def profile_display (request):
    un=request.session.get('username')
    UO=User.objects.get(username=un)
    PO=profile.objects.get(name=UO)
    d={'UO':UO,'PO':PO}
    return render (request,'profile_display.html',d)

        