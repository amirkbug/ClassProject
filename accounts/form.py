from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120,widget=forms.PasswordInput)
    
class SignupForm(UserCreationForm):
    email = forms.EmailField()
    
class Change_passwordForm(forms.Form):
    current_password = forms.CharField(max_length=120,widget=forms.PasswordInput)
    password = forms.CharField(max_length=120,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=120,widget=forms.PasswordInput)
    
class ResetpasswordForm(forms.Form):
    email = forms.EmailField()
    
class ResetpaswordconfirmForm(forms.Form):
    pass1 = forms.CharField(max_length=120,widget=forms.PasswordInput)
    pass2 = forms.CharField(max_length=120,widget=forms.PasswordInput)