from django.db import models
import os
import hashlib
from django.contrib.auth.models import User


class RegisterToken(models.Model):
    token = models.CharField(max_length=40, unique=True)
    use = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        ordering = (('use'), ('-created_at'))

    def __str__(self):
        return self.token

    def save(self, *args, **kargs):
        if not self.token:
            try:
                self.token = hashlib.sha1(os.urandom(128)).hexdigest()
                super(RegisterToken, self).save(*args, **kargs)
            except:
                return self.save()
        else:
            super(RegisterToken, self).save(*args, **kargs)
