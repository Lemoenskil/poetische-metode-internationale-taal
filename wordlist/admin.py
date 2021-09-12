from django.contrib import admin
from .models import Acronym, PartOfSpeach, Word
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from translated_fields import TranslatedFieldAdmin

# Register your models here.
@admin.register(Acronym)
class AcronymAdmin(NestedModelAdmin):
    pass

@admin.register(PartOfSpeach)
class PartOfSpeachAdmin(TranslatedFieldAdmin, NestedModelAdmin):
    pass

@admin.register(Word)
class WordAdmin(TranslatedFieldAdmin, NestedModelAdmin):
    pass
