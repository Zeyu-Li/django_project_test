from django.shortcuts import render
from .forms import UserpassForm

def home(request):

    return render(request, 'userpass/home.html')

def login(request):

    if request.method == 'POST':
        filled_form = UserpassForm(request.POST)
        if filled_form.is_valid():

            note = 'You have logged in successfully %s' %filled_form.cleaned_data['username']
            new_form = UserpassForm()
            return render(request, 'userpass/login.html', {'UserpassForm':new_form, 'note': note})

    else:

        form = UserpassForm()
        return render(request, 'userpass/login.html', {'UserpassForm':form})