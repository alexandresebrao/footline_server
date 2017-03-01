from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    class Meta:
        ordering = (("-date"),)

    def __str__(self):
        return self.title
