from django.shortcuts import render, get_object_or_404
from .models import Poem

# Create your views here.
def poems(request):
    """A view that displays the poems page"""
    return render(request, "poems.html")

def single_poem(request, id):
    """A view that displays a single poem"""
    poem = get_object_or_404(Poem, pk=id)
    return render(request, "single-poem.html", { 'poem': poem })