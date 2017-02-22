from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.utils import timezone
import hashlib


class UserAddon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    token = models.CharField(max_length=40, blank=True, null=True)
    valid = models.DateTimeField(blank=True, null=True)
    friends = models.ManyToManyField(User, related_name='Friends')
    channel = models.CharField(max_length=100, null=True, blank=True)

    def get_token(self):
        if not self.token:
            token = ("%s,%s" % (self.user.username,
                                timezone.now())).encode('utf-8')
            self.token = hashlib.md5(token).hexdigest()
            self.valid = timezone.now() + timezone.timedelta(days=1)
        if self.valid < timezone.now():
            token = ("%s,%s" % (self.user.username,
                                timezone.now())).encode('utf-8')
            self.token = hashlib.md5(token).hexdigest()
            self.valid = timezone.now() + timezone.timedelta(days=1)
        self.save()
        return self.token
