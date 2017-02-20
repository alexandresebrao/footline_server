from channels import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models.register import RegisterToken


@receiver(post_save, sender=RegisterToken)
def send_update(sender, instance, created, **kwargs):
    if created:
        text = "rt:add:%s" % instance.id
    else:
        text = "rt:update:%s" % instance.id
    data = {'text': text}
    Group("admin").send(data)
