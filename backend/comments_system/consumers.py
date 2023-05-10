import json

from channels.generic.websocket import WebsocketConsumer


class MainConsumer(WebsocketConsumer):
    def connect(self):
        print("connect!", self.channel_name)
        self.channel_layer.group_add("main", self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        if text_data is None:
            return

        data = json.loads(text_data)
        print(data)
        # self.channel_layer.group_send("main", data)
        self.send(text_data)
