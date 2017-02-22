# In consumers.py
from channels import Group
from core.models.user import UserAddon


# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})


def ws_message(message):
    def ws_message(message):
        token = message.content['text'].replace('token:', '')
        try:
            UserAddon.objects.get(token=token)
            Group("admin").add(message.reply_channel)
            Group("broadcast").add(message.reply_channel)
        except:
            Group("broadcast").add(message.reply_channel)


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("boadcast").discard(message.reply_channel)
    Group("admin").discard(message.reply_channel)
