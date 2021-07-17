from django.db import models
from django.db.models.base import Model
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField
from filer.fields.image import FilerImageField
import datetime
from django.utils import timezone

class Genre(models.Model):
    name = TranslatedField(
        models.CharField(_("name"), max_length=254, default='')
    )

    def __str__(self):
        return self.name

class Country(models.Model):
    name = TranslatedField(
        models.CharField(_("name"), max_length=254, default='')
    )

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

# Create your models here.
class Author(models.Model):
    name = TranslatedField(
        models.CharField(_("name"), max_length=254, default='')
    )
    date_of_birth = models.DateField(default=datetime.date.today)
    date_of_death = models.DateField(blank=True, null=True)
    country_of_birth = models.ForeignKey(Country, related_name='authors', on_delete=models.CASCADE, null=True)
    portrait = FilerImageField(related_name='authors', null=True, blank=True, on_delete=models.SET_NULL)
    abstract = TranslatedField(
        models.TextField(_("abstract"), default='')
    )

    def __str__(self):
        return self.name

class Poem(models.Model):
    featured = models.BooleanField(default=False)
    author = models.ForeignKey(Author, related_name='poems', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name='poems', on_delete=models.CASCADE, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    image = FilerImageField(related_name='poems', null=True, blank=True, on_delete=models.SET_NULL)
    abstract = TranslatedField(
        models.TextField(_("abstract"), default='', blank=True)
    )

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
