from . import WebSocket
from listeners.tick import GameThread

class WebSocketThread:
    def __init__(self, url, cb=None):
        self.cb = cb
        self.thread = None
        self.url = url
        self.socket = None

    def start(self):
        self.socket = WebSocket(url=''.join(self.url), cb=self.cb)
        self.thread = GameThread(target=self.socket.start_socket_connection)
        self.thread.start()
    
    def stop(self):
        if self.thread != None:
            self.socket.stop()
            self.thread._stop()
