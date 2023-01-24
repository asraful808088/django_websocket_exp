import json

from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class ChatWebsocket(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send(
            {
                "type":"websocket.accept"
            }
        )


    async def websocket_disconnect(self,event):
        raise StopConsumer()


    async def websocket_receive(self,event):
         info = {
            "name":self.channel_name,
         }
         await self.send(
            {
                "type":"websocket.send",
                'text':json.dumps(info)
            }
        )
