from django.shortcuts import render, get_object_or_404
from .models import Poem, Genre, Author, Country

# Create your views here.
def poems(request):
    """A view that displays the poems page"""
    poems = Poem.objects.all()
    genres = Genre.objects.all()
    authors = Author.objects.all()
    countries = Country.objects.all()
    return render(request, "poems.html", {
        'poems': poems,
        'genres': genres,
        'authors': authors,
        'countries': countries
    })

def single_poem(request, id):
    """A view that displays a single poem"""
    poem = get_object_or_404(Poem, pk=id)
    return render(request, "single-poem.html", { 'poem': poem })