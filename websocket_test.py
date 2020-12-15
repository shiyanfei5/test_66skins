import ssl
import time
import threading
import websocket


# def on_message(ws, message):
#     print(message)
#
# def on_error(ws, error):
#     print(error)
#
# def on_close(ws):
#     print("### closed ###")
#
# def on_open(ws):
#     def run(*args):
#         for i in range(3):
#             time.sleep(1)
#             ws.send("Hello %d" % i)
#         time.sleep(1)
#         ws.close()
#         print("thread terminating...")
#     threading.Thread(target=run)
#
#
# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("ws://echo.websocket.org/",
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()
from websocket import ABNF

from common.stamp_utils import send_frame, CMD_CONNECT


class WebSocketClient(object):

    def __init__(self, address, if_trace):
        self.address = address
        websocket.enableTrace(if_trace)
        self.ws = websocket.WebSocketApp(self.address,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         on_open=self.on_open)
        self.ws.run_forever()

    def on_message(self,  message):
        print(message)

    def on_error(self,  error):
        print(error)


    def on_close(self):
        print("### closed ###")

    def on_open(self):
        print("### open ###")
        ws = self.ws

        def run(*args):
                result = send_frame(CMD_CONNECT, {
                    "accept-version": "1.1",
                    "heart-beat": "10000,10000"
                })
                print(result)
                # ws.send(result, ABNF.OPCODE_BINARY)
                ws.send('CONNECT\naccept-version:1.1\nheart-beat:10000,10000"')
                time.sleep(1)
                # ws.send("SUBSCRIBE\nid:sub-0\ndestination:/user/notice\n\n\u0000")
                time.sleep(1)
                # ws.send("SUBSCRIBE\nid:sub-1\ndestination:/user-message/20083622/web\n\n\u0000")
                time.sleep(1)
                # ws.send("SUBSCRIBE\nid:sub-2\ndestination:/check/net/20083622\n\n\u0000")
                time.sleep(1)

        t = threading.Thread(target=run)
        t.start()


socket_client = WebSocketClient("wss://api.66skins.com/users-ws/websocket/323/kgyhw40w/websocket?token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIyMDA4MzYyMiIsInN5c3RlbXR5cGUiOiJ3ZWIiLCJleHAiOjE2MDgxMzU2MzEsInVzZXJpZCI6bnVsbCwiY3JlYXRlZCI6MTYwODA0OTIzMTQ3NCwiYXV0aG9yaXRpZXMiOlt7ImF1dGhvcml0eSI6InNob3dSb2xsVXNlciJ9XX0.6v9oa40gPCT6WLEykljxxvwS3A413-NnnMb6wR-JkyGhRyR4iFgGGdrZyt-oTaUN2bssNkazDbrZv4IowAK9vw", True)

