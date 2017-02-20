from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class UserAddon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid4, editable=False)
    online = models.BooleanField(default=True)
