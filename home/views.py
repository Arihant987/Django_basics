from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # sort of mapping is there
    context={ 
        "variable":"keklamo variable",
        "x":"4",
        "y":"3"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        email= request.POST.get('email')
        password= request.POST.get('password')
        contact=Contact(email=email,password=password,date=datetime.today())
        contact.save()
        messages.success(request, "Your info has been stored")
    return render(request,'contact.html')