from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput) # widget gives the *** in pw
    email = forms.EmailField()

    class Meta: # basically gives information about your class 
        models = User
        fields = ['username','email','password']