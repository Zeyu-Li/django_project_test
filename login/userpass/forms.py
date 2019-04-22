from django import forms
from .models import User

# class UserpassForm(forms.Form):

#     username = forms.CharField(label='Username', max_length=100) 

#     password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput) 

class UserpassForm(forms.ModelForm):
    class Meta:
        model = Pass
        fields = ['password']
