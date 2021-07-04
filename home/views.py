from blogs.models import Blog
from django.shortcuts import render, redirect, reverse
from poems.models import Poem 
from blogs.models import Blog
from django.utils import timezone

# Create your views here.
def index(request):
    """A view that displays the index page"""
    poems = Poem.objects.all()
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "index.html", {
        'poems': poems,
        'blogs': blogs,
    })    

def about(request):
    """A view that displays the about page"""
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, "about.html", {'blogs': blogs})

def learning_methode(request):
    """A view that displays the learning_methode page"""
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, "learning_methode.html",{'blogs': blogs})   

def contact(request):
    """A view that displays the contact page"""
    return render(request, "contact.html") 