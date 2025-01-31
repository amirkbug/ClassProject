from django import forms
from .models import Contactus

class Contactusform(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['name','email','subject','message']