from django.shortcuts import render

# Create your views here.
def poems(request):
    """A view that displays the index page"""
    return render(request, "poems.html")
