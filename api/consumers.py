# In consumers.py
from channels import Group

# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("admin").add(message.reply_channel)


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("admin").discard(message.reply_channel)
