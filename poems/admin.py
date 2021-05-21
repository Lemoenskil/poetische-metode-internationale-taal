from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from .models import Poem, Title, Stanza, Line

class LineInline(NestedTabularInline):
    model = Line
    extra = 0
class TitleInline(NestedTabularInline):
    model = Title
    extra = 1
    max_num = 1
    min_num = 1
class StanzaInline(NestedTabularInline):
    model = Stanza
    inlines = [
        LineInline,
    ]
    extra = 0

# Register your models here.
@admin.register(Poem)
class PoemAdmin(NestedModelAdmin):
    inlines = [
        TitleInline,
        StanzaInline,
    ]
