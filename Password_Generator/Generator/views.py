from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'Generator/home.html')

def password(request):
    return render(request,'Generator/password.html')