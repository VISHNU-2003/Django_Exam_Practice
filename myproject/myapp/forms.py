from django import forms
from django.shortcuts import render
from .models import Practice

class InputForm1(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=40)
    password = forms.CharField(widget = forms.PasswordInput)
    
#creating class for signupform and storing the details in my database
class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice 
        fields = ['name', 'email', 'password']