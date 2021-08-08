import websocket

class WebSocket:
    def __init__(self, url, cb=None):
        self.url = url
        self.running = True
        self.ws = None
        self.cb = cb

    def start_socket_connection(self):
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(self.url,
                                on_open=self.on_open,
                                on_message=self.on_message if self.cb == None else self.cb,
                                on_error=self.on_error,
                                on_close=self.on_close)
        self.running = True
        self.ws.run_forever()

    def on_open(self, ws):
        print("Connection opened")
        return

    def on_message(self, ws, message):
        pass

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print("Connection closed")
        if self.running:
            print('Trying to reconnect')
            self.start_socket_connection()
        else:
            self.running = False
    
    def stop(self):
        self.running = False
        self.ws.keep_running = False
        self.ws.close()