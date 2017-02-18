from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.utils import timezone


class UserAddon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid4, editable=False)
    online = models.DateTimeField(blank=True, null=True)

    def is_online(self):
        return (self.online and self.online > timezone.now())
