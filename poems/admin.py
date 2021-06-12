from django.contrib import admin
from translated_fields import TranslatedFieldAdmin
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from .models import Country, Author, Poem, Title, Stanza, Line

@admin.register(Country)
class CountryAdmin(TranslatedFieldAdmin, NestedModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(TranslatedFieldAdmin, NestedModelAdmin):
    pass

class LineInline(TranslatedFieldAdmin, NestedTabularInline):
    model = Line
    extra = 0

class TitleInline(TranslatedFieldAdmin, NestedTabularInline):
    model = Title
    extra = 1
    max_num = 1
    min_num = 1

class StanzaInline(TranslatedFieldAdmin, NestedTabularInline):
    model = Stanza
    inlines = [
        LineInline,
    ]
    extra = 0

# Register your models here.
@admin.register(Poem)
class PoemAdmin(TranslatedFieldAdmin, NestedModelAdmin):
    inlines = [
        TitleInline,
        StanzaInline,
    ]
