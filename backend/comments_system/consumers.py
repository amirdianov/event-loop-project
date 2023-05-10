import json

from channels.generic.websocket import AsyncWebsocketConsumer

from users_event.models import Event


class MainConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connect!", self.channel_name)
        room_id = self.scope["url_route"]["kwargs"]["room"]
        is_event_exist = await Event.objects.filter(id=room_id).aexists()
        if not is_event_exist:
            await self.close()
            return
        await self.channel_layer.group_add(room_id, self.channel_name)
        await self.accept()

        event = await Event.objects.filter(id=room_id).aget()

        await self.send(json.dumps({"event_title": event.title}))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard("main", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        if text_data is None:
            return

        data = json.loads(text_data)
        print(data)
        # self.channel_layer.group_send("main", data)
        await self.send(text_data)
        # Send message to room group

        await self.channel_layer.group_send(
            self.scope["url_route"]["kwargs"]["room"],
            {"type": "chat_message", "message": data["message"]},
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
