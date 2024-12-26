import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CalculatorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'calculator_room'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        expression = text_data_json['expression']
        
        # You can use eval or another safe method for calculation
        try:
            result = eval(expression)
        except Exception as e:
            result = 'Error'
        
        await self.send(text_data=json.dumps({
            'result': result
        }))
