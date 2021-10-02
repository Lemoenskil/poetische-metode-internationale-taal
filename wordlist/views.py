from django.shortcuts import render
from .models import Acronym, WordGroup

def wordlist (request):
    """A view that displays the contact page"""
    acronyms = Acronym.objects.all()

    return render(request, "wordlist.html", {
        'acronyms': acronyms,
    }) 

