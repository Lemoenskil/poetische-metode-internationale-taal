from django.db import models
from django.utils import timezone
from filer.fields.image import FilerImageField

class Blog(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    image = FilerImageField(related_name='img', null=True, blank=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title + ' - ' + self.author
