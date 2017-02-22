from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.utils import timezone


class UserAddon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(blank=True, null=True)
    online = models.BooleanField(default=True)
    valid = models.DateTimeField(blank=True, null=True)

    def get_token(self):
        if not self.token:
            self.token = uuid4
            self.valid = timezone.now() + timezone.timedelta(days=1)
        if self.valid < timezone.now():
            self.token = uuid4
            self.valid = timezone.now() + timezone.timedelta(days=1)
        self.save()
        return self.token
