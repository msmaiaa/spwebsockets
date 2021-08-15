import websocket
import time

class WebSocket:
    def __init__(self, url, cb_on_message=None, cb_on_open=None, cb_on_close=None, cb_on_error=None):
        self.url = url
        self.running = True
        self.ws = None
        self.cb_on_message = cb_on_message
        self.cb_on_open = cb_on_open
        self.cb_on_close = cb_on_close
        self.cb_on_error = cb_on_error

    def start_socket_connection(self):
        websocket.enableTrace(False)
        if self.ws != None:
            self.ws.close()
            self.ws = None
        self.ws = websocket.WebSocketApp(self.url,
                                on_open=self.on_open if self.on_open == None else self.cb_on_open,
                                on_message=self.on_message if self.on_message == None else self.cb_on_message,
                                on_error=self.on_error if self.on_error == None else self.cb_on_error,
                                on_close=self.on_close
                                )
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
        if self.running:
            print('Connection lost')
            time.sleep(10)
            print('Trying to reconnect')
            self.start_socket_connection()
        else:
            self.running = False
        
        if self.on_close is not None:
            self.cb_on_close(ws, close_status_code, close_msg)
    
    def stop(self):
        self.running = False
        self.ws.keep_running = False
        self.ws.close()