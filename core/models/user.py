from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class UserAddon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    valid = models.DateTimeField(blank=True, null=True)
    friends = models.ManyToManyField(User, related_name='Friends')

    def online(self):
        return (self.user.userchannel_set.count() > 0)


class UserChannel(models.Model):
    channel = models.CharField(max_length=30)
    user = models.ForeignKey(User)
