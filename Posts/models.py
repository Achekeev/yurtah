from django.db import models
from Users.models import User


class Posts(models.Model):
    owner = models.ForeignKey('Blog', on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.text
# Create your models here.
