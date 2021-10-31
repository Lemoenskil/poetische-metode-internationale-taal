from django.contrib import admin
from translated_fields import TranslatedFieldAdmin
from nested_admin import NestedModelAdmin
from .models import VoiceRecording

# Register your models here.
@admin.register(VoiceRecording)
class VoiceRecordingAdmin(TranslatedFieldAdmin, NestedModelAdmin):
    pass
