from django.db import models
import os
import hashlib


class RegisterToken(models.Model):
    token = models.CharField(max_length=40, unique=True)
    use = models.BooleanField(default=False)

    def save(self, *args, **kargs):
        if not self.token:
            try:
                self.token = hashlib.sha1(os.urandom(128)).hexdigest()
                super(RegisterToken, self).save(*args, **kargs)
            except:
                return self.save()
