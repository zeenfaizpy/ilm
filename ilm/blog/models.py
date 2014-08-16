from django.db import models
from django.template.defaultfilters import slugify

from helpers.models import TimestampedModel

class Tag(models.Model):
    """
    Represents the tags for posts.
    """
    name = models.CharField(max_length=120)

    def __unicode__(self):
        """
        Returns the human readable object name.
        """
        return self.name


class Category(models.Model):
    """
    Represents the category of posts.
    """
    name = models.CharField(max_length=120)

    def __unicode__(self):
        """
        Returns the human readable object name.
        """
        return self.name


class Post(TimestampedModel):
    """
    Holds all posts of a blog.
    """
    title = models.CharField(max_length=120, blank=False)
    content = models.TextField()
    slug = models.SlugField(max_length=120, unique=True, blank=False)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=False)
    category = models.ForeignKey(Category, related_name="posts", blank=False)

    def save(self, *args, **kwargs):
        """
        Overriding save method to slugify.
        """
        # if not self.slug:
        #     self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        """
        return reverse_lazy('detail_post', kwargs={'slug': self.slug})

    def __unicode__(self):
        """
        Returns the human readable object name.
        """
        return self.title