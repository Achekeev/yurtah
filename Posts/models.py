from django.db import models
from Users.models import User
from Blog.models import Blog


class Posts(models.Model):
    owner = models.ForeignKey('Blog', on_delete=models.CASCADE, blank=True, null=True)
    post = models.CharField( on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.blog
# Create your models here.
