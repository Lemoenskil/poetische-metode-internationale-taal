from django.db import models
from django.db.models.base import Model
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField

    
# Create your models here.
class Author(models.Model):
    name = TranslatedField(
        models.CharField(_("name"), max_length=254, default='')
    )

    def __str__(self):
        return self.name

class Poem(models.Model):
    author = models.ForeignKey(Author, related_name='poems', on_delete=models.CASCADE)

    def __str__(self):
        return ' - '.join([
            self.title.all()[0].title,
            self.author.name,
        ])

class Title(models.Model):
    poem = models.ForeignKey(Poem, related_name='title', on_delete=models.CASCADE)
    title = TranslatedField(
        models.CharField(_("title"), max_length=254, default='')
    )

class Stanza(models.Model):
    poem = models.ForeignKey(Poem, related_name='stanzas', on_delete=models.CASCADE)

class Line(models.Model):
    stanza = models.ForeignKey(Stanza, related_name='lines', on_delete=models.CASCADE)
    line = TranslatedField(
        models.CharField(_("line"), max_length=1024, default='')
    )
