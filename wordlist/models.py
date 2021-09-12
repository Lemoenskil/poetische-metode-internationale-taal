from django.db import models
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField

# Create your models here.
class Acronym(models.Model):
    first_letter = models.CharField(_("first_letter"), max_length=1)

    def __str__(self):
        return self.first_letter

class PartOfSpeach(models.Model):
    name = TranslatedField(
        models.CharField(_("name"), max_length=254, default='')
    )

    class Meta:
        verbose_name_plural = "PartsOfSpeach"

    def __str__(self):
        return self.name

class Word(models.Model):
    word = TranslatedField(
        models.CharField(_("word"), max_length=254, default='')
    )
    acronym = models.ForeignKey(Acronym, related_name='words', on_delete=models.CASCADE, null=True)
    part_of_speach = models.ForeignKey(PartOfSpeach, related_name='words', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.word
