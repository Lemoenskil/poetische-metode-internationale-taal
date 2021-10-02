from django.db import models
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField

# Create your models here.
class Acronym(models.Model):
    first_letter = models.CharField(_("first_letter"), max_length=1)

    def __str__(self):
        return self.first_letter

class WordGroup(models.Model):
    acronym = models.ForeignKey(Acronym, related_name='word_groups', on_delete=models.CASCADE, null=True)

class Noun(models.Model):
    word_group = models.ForeignKey(WordGroup, related_name='noun', on_delete=models.CASCADE, null=True)
    noun = TranslatedField(
        models.CharField(_("word"), max_length=254, default='', blank=True)
    )

class Misc(models.Model):
    word_group = models.ForeignKey(WordGroup, related_name='misc', on_delete=models.CASCADE, null=True)
    misc = TranslatedField(
        models.CharField(_("word"), max_length=254, default='', blank=True)
    )

class Verb(models.Model):
    word_group = models.ForeignKey(WordGroup, related_name='verb', on_delete=models.CASCADE, null=True)
    verb = TranslatedField(
        models.CharField(_("word"), max_length=254, default='', blank=True)
    )

