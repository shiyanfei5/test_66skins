import stomp
import websocket

from common.stomp_utils import send_frame, CMD_CONNECT, CMD_SUBSCRIBE
from common.user import User


class WebSocketClient(object):

    def __init__(self, address, if_trace= False):
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

        result = send_frame(CMD_CONNECT, {
            "accept-version": "1.1,1.0",
            "heart-beat": "10000,10000"
        })
        self.ws.send(result)

        result = send_frame(CMD_SUBSCRIBE, {
            "id": "sub-0",
            "destination": "/user/notice"
        })
        self.ws.send(result)
        result = send_frame(CMD_SUBSCRIBE, {
            "id": "sub-1",
            "destination": "/user-message/20083622/web"
        })
        self.ws.send(result)
        result = send_frame(CMD_SUBSCRIBE, {
            "id": "sub-2",
            "destination": "/check/net/20083622"
        })
        self.ws.send(result)





socket_client = WebSocketClient("ws://www.ynkyt.cn/boxs/users-ws/websocket/728/s14rg2nm/websocket?token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI1MTg2NzIxMiIsInN5c3RlbXR5cGUiOiJ3ZWIiLCJleHAiOjE2MDgyMDUyMjAsInVzZXJpZCI6bnVsbCwiY3JlYXRlZCI6MTYwODExODgyMDMwNSwiYXV0aG9yaXRpZXMiOlt7ImF1dGhvcml0eSI6InNob3dSb2xsVXNlciJ9XX0.WU7W3NqxR-Z96zL6ayulRzHP6d4QfsRpCe-fq854DGPmCH1UQZqRDAQpc6vWWqJ7kMPPgTzWrggKfwfQzVZOOA", True)


class SkinsSocketUserClient(object):

    def __init__(self, user, wss_addr):
        self.user = User()
        self.ws_addr = wss_addr
        self._socket_client = WebSocketClient(wss_addr)
        stomp.Connection11
















