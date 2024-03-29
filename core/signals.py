from channels import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models.register import RegisterToken
from core.models.user import UserChannel
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@receiver(post_save, sender=RegisterToken)
def send_token_update(sender, instance, created, **kwargs):
    if created:
        text = "rt:add:%s" % instance.id
    else:
        text = "rt:update:%s" % instance.id
    data = {'text': text}
    Group("admin").send(data)


@receiver(post_save, sender=UserChannel)
def send_user_status(sender, instance, **kwargs):
    if instance.channel:
        text = "user:online:%s" % instance.user.useraddon.uuid
    else:
        text = "user:offline:%s" % instance.user.useraddon.uuid
    data = {'text': text}
    Group("broadcast").send(data)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
