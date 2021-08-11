from . import WebSocket
from listeners.tick import GameThread

class WebSocketThread:
    def __init__(self, url, on_message=None, on_open=None, on_close=None, on_error=None):
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.on_error = on_error
        self.thread = None
        self.url = url
        self.socket = None

    def start(self):
        self.socket = WebSocket(url=''.join(self.url), on_message=self.on_message, on_open=self.on_open, on_close=self.on_close, on_error=self.on_error)
        self.thread = GameThread(target=self.socket.start_socket_connection)
        self.thread.start()
    
    def stop(self):
        if self.thread != None:
            self.socket.stop()
            self.thread._stop()
