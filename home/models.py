from django.db import models
from translated_fields import TranslatedField
from django.utils.translation import gettext_lazy as _

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

# Create your models here.
class SiteSettings(SingletonModel):
    """
    The site settings
    """
    introduction = TranslatedField(
        models.TextField(_("introduction"), default='', blank=True)
    )
