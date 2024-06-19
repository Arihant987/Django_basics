from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.html')