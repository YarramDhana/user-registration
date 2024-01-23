from app.models import *
from django import forms

class Userforms (forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
       
        help_texts={'username':''}



class profileforms (forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']
        