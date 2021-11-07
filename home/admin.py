from django.contrib import admin
from translated_fields import TranslatedFieldAdmin
from nested_admin import NestedModelAdmin
from .models import SiteSettings

# Register your models here.
@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslatedFieldAdmin, NestedModelAdmin):
    pass
