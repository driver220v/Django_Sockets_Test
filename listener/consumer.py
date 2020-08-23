import json
from channels.generic.websocket import WebsocketConsumer


class Socket(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'message': f'hi'
        }))

    def disconnect(self, close_code):
        pass

