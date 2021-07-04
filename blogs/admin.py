from django.contrib import admin

# Register your models here.
from translated_fields import TranslatedFieldAdmin
from nested_admin import NestedModelAdmin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(TranslatedFieldAdmin, NestedModelAdmin):
    pass

