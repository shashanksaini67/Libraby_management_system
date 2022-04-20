from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def AdminSignup(request):
    return render(request, 'AdminSignup.html')


def AdminLogin(request):
    return render(request, 'AdminLogin.html')


def StudentSignin(request):
    return render(request, 'Studentsignin.html')
