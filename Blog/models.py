from django.db import models
from Users.models import User
from Posts.models import Posts


class Blog(models.Model):
    owner = models.OneToOneField('User', on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey('Posts', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.blog
# Create your models here.
