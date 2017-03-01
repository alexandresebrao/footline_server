# In consumers.py
from channels import Group
from core.models.user import UserChannel
from rest_framework.authtoken.models import Token


# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})


def ws_message(message):
    token = message.content['text'].replace('token:', '')
    try:
        user = Token.objects.get(key=token).user
        user.useraddon.save()
        user.userchannel_set.create(user=user, channel=message.reply_channel)
        Group("broadcast").add(message.reply_channel)
        Group("user-%s" % user.id).add(message.reply_channel)
        if user.is_staff:
            Group("admin").add(message.reply_channel)
    except:
        Group("broadcast").add(message.reply_channel)


# Connected to websocket.disconnect
def ws_disconnect(message):
    channel = message.reply_channel
    try:
        uc = UserChannel.objects.get(channel=channel)
        user = uc.user
        uc.delete()
        Group("user-%s" % user.id).discard(channel)
        Group("boadcast").discard(channel)
    except:
        Group("boadcast").discard(channel)
    Group("admin").discard(channel)
