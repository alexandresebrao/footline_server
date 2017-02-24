# In consumers.py
from channels import Group
from core.models.user import UserAddon


# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})


def ws_message(message):
    token = message.content['text'].replace('tn:', '')
    try:
        useraddon = UserAddon.objects.get(token=token)
        useraddon.channel = message.reply_channel
        useraddon.save()
        user = useraddon.user
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
        useraddon = UserAddon.objects.get(channel=channel)
        useraddon.channel = ""
        useraddon.save()
        user = useraddon.user
        Group("user-%s" % user.id).discard(channel)
    except:
        Group("boadcast").discard(channel)
    Group("boadcast").discard(channel)
    Group("admin").discard(channel)
