from django.shortcuts import render
from .models import Acronym, PartOfSpeach, Word

def wordlist (request):
    """A view that displays the contact page"""
    acronyms = Acronym.objects.all()
    parts_of_speech = PartOfSpeach.objects.all()

    return render(request, "wordlist.html", {
        'acronyms': acronyms,
        'parts_of_speech': parts_of_speech,
    }) 

