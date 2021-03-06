from django.shortcuts import render
from .models import VoiceRecording

# Create your views here.
def get_audio(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'audio.html' template
    """
    voice_recordings = VoiceRecording.objects.all()
    return render(request, "audio.html", {
        'voice_recordings': voice_recordings
    })
