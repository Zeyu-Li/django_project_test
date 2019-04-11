from django.shortcuts import render

def home(request):

    return render(request, 'userpass/home.html')

def login(request):

    return render(request, 'userpass/login.html')