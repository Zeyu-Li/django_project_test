from django import forms
from .models import User

# class UserpassForm(forms.Form):

#     username = forms.CharField(label='Username', max_length=100) 

password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput) 
