from django.db import models
from django.template.defaultfilters import slugify

from helpers.models import TimestampedModel

class Tag(models.Model):
    """
    Represents the tags for posts.
    """
    name = models.CharField(max_length=120)


class Category(models.Model):
    """
    Represents the category of posts.
    """
    name = models.CharField(max_length=120)


class Post(TimestampedModel):
    """
    Holds all posts of a blog.
    """
    title = models.CharField(max_length=120, blank=False)
    content = models.TextField()
    slug = models.SlugField(max_length=120, unique=True)
    tags = models.ManyToManyField(Tag, related_name="posts")
    category = models.ForeignKey(Category, related_name="posts")

    def __unicode__(self):
        """
        Returns the human readable object name.
        """
        return self.title