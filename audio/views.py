from django.shortcuts import render

# Create your views here.
def get_audio(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'audio.html' template
    """
    return render(request, "audio.html")
