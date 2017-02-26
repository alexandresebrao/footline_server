from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.utils import timezone
import hashlib


class UserAddon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    valid = models.DateTimeField(blank=True, null=True)
    friends = models.ManyToManyField(User, related_name='Friends')
    channel = models.CharField(max_length=100, null=True, blank=True)
