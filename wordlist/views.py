from django.shortcuts import render

def wordlist (request):
    """A view that displays the contact page"""
    return render(request, "wordlist.html") 
