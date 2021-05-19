from django.shortcuts import render, redirect, reverse 


# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")    

def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")  

def contact(request):
    """A view that displays the contact page"""
    return render(request, "contact.html") 