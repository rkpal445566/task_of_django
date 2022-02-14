from django import forms
from django.forms import widgets
from app_1.models import User

class Student(forms.ModelForm):
    class Meta:
       model=User
       fields=['name','Email','password']
       widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                'Email':forms.EmailInput(attrs={'class':'form-control'}),
                'password':forms.PasswordInput(attrs={'class':'form-control'})
            }
        
