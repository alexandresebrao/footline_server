import os
import channels.asgi
from whitenoise.django import DjangoWhiteNoise
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "footline.settings")
channel_layer = channels.asgi.get_channel_layer()
if settings.HEROKU:
    application = DjangoWhiteNoise(channel_layer)
