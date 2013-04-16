from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
