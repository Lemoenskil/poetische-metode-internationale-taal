from django.shortcuts import render
from django.db.models import CharField, TextField
from django.db.models import Q
from poems.models import Poem, Author, Genre, Line
from blogs.models import Blog

def any_model_string_field_containing(model, string, prefix=None):
    prefix = '' if prefix is None else f'{prefix}__'
    fields = [ x for x in model._meta.fields if isinstance(x, CharField) or isinstance(x, TextField) ]
    queries = [ Q( **{ f'{prefix}{x.name}__icontains': string } ) for x in fields ]
    q_any_of = Q()
    for q in queries:
        q_any_of = q_any_of | q
    return q_any_of

# Create your views here.
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]

        blogs = Blog.objects.filter(
            any_model_string_field_containing(Blog, searched)
        )

        poems = Poem.objects.filter(
            any_model_string_field_containing(Poem, searched) |
            any_model_string_field_containing(Author, searched, 'author') |
            any_model_string_field_containing(Genre, searched, 'genre') |
            any_model_string_field_containing(Line, searched, 'stanzas__lines')
        ).distinct()

        return render(request, "search_results.html", {
            'searched': searched,
            'blogs': blogs,
            'poems': poems,
        })
    else:
        return render(request, "search_results.html")

