from django.db import models
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField
from filer.fields.file import FilerFileField

# Create your models here.
class VoiceRecording(models.Model):
    title = TranslatedField(
        models.CharField(_("name"), max_length=254, default='')
    )
    audio_file = FilerFileField(related_name='audio_file', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
