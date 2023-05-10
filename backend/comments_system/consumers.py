from channels.generic.websocket import WebsocketConsumer


class MainConsumer(WebsocketConsumer):
    def connect(self):
        print("Connect!")
        self.accept()
