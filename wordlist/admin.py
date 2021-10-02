from django.contrib import admin
from .models import Acronym, Noun, Misc, Verb, WordGroup
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from translated_fields import TranslatedFieldAdmin

# Register your models here.
class NounInline(TranslatedFieldAdmin, NestedTabularInline):
    model = Noun
    extra = 1
    max_num = 1
    min_num = 1

class MiscInline(TranslatedFieldAdmin, NestedTabularInline):
    model = Misc
    extra = 1
    max_num = 1
    min_num = 1

class VerbInline(TranslatedFieldAdmin, NestedTabularInline):
    model = Verb
    extra = 1
    max_num = 1
    min_num = 1

class WordGroupInline(TranslatedFieldAdmin, NestedStackedInline):
    model = WordGroup
    inlines = [
        NounInline,
        MiscInline,
        VerbInline,
    ]
    extra = 0

@admin.register(Acronym)
class AcronymAdmin(TranslatedFieldAdmin, NestedModelAdmin):
    inlines = [
        WordGroupInline,
    ]
    extra = 0
    