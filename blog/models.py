from django.db import models
from organizer.models import Startup, Tag

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)

    def __str__(self):
        return "{}:{}".format(
            self.title, self.pub_date.strftime('%Y-%m-%d'))

        class Meta:
            verbose_name = 'blog post'
            ordering = ['-pub_date', 'title']
            get_latest_by = 'pub_date'
