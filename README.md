# spwebsockets
### This a simple threaded websocket wrapper for Source.Python 

#### How to install?
- Just clone the repository into the /addons/source-python/packages/custom folder

Usage example:
```python
from spwebsockets.WebSocketThread import WebSocketThread

from messages import SayText2
websocket_thread = None


def load():
    global websocket_thread
    # as you can see, the callback that you set will receive all the messages, including the websocket handle
    websocket_thread = WebSocketThread(url="ws://10.0.0.159:5000/websockets", cb=handle_socket_message)
    websocket_thread.start()

def unload():
    global websocket_thread
    websocket_thread.stop()


def handle_socket_message(ws, message):
    SayText2(message).send()
```
