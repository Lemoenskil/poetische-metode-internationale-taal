from django.db import models
from django.db.models.base import Model

# Create your models here.
class Poem(models.Model):
    author = models.CharField(max_length=254, default='')

    def __str__(self):
        return ' - '.join([
            self.title.all()[0].title,
            self.author,
        ])

class Title(models.Model):
    poem = models.ForeignKey(Poem, related_name='title', on_delete=models.CASCADE)
    title = models.CharField(max_length=254, default='')

class Stanza(models.Model):
    poem = models.ForeignKey(Poem, related_name='stanzas', on_delete=models.CASCADE)

class Line(models.Model):
    stanza = models.ForeignKey(Stanza, related_name='lines', on_delete=models.CASCADE)
    line = models.CharField(max_length=1024, default='')
