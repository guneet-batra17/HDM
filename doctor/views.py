from django.shortcuts import render, HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.hashers import PBKDF2SHA1PasswordHasher

def doctorindex(request):
    return render(request,'doctorindex.html')

# Create your views here.
