from django.shortcuts import render

def index(request):
    return render(request, "reservation/home.html")

# Create your views here.
