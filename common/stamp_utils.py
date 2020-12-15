from stomp import utils
from stomp.utils import convert_frame, pack, encode, HDR_CONTENT_LENGTH

CMD_ABORT = "ABORT"
CMD_ACK = "ACK"
CMD_BEGIN = "BEGIN"
CMD_COMMIT = "COMMIT"
CMD_CONNECT = "CONNECT"
CMD_DISCONNECT = "DISCONNECT"
CMD_NACK = "NACK"
CMD_STOMP = "STOMP"
CMD_SEND = "SEND"
CMD_SUBSCRIBE = "SUBSCRIBE"
CMD_UNSUBSCRIBE = "UNSUBSCRIBE"
ENC_NEWLINE = encode("\n")
ENC_NULL = b""



def convert_frame(frame):
    """
    Convert a frame to a list of lines separated by newlines.

    :param Frame frame: the Frame object to convert

    :rtype: list(str)
    """
    lines = []

    body = None
    if frame.body:
        body = encode(frame.body)

        if HDR_CONTENT_LENGTH in frame.headers:
            frame.headers[HDR_CONTENT_LENGTH] = len(body)

    if frame.cmd:
        lines.append(encode(frame.cmd))
        lines.append(ENC_NEWLINE)
    for key, vals in sorted(frame.headers.items()):
        if vals is None:
            continue
        if type(vals) != tuple:
            vals = (vals,)
        for val in vals:
            lines.append(encode("%s:%s\n" % (key, val)))
    lines.append(ENC_NEWLINE)
    if body:
        lines.append(body)

    if frame.cmd:
        lines.append(ENC_NULL)
    return lines




def send_frame(cmd, headers=None, body=''):
    """
    Encode and send a stomp frame
    through the underlying transport.

    :param str cmd: the protocol command
    :param dict headers: a map of headers to include in the frame
    :param body: the content of the message
    """
    frame = utils.Frame(cmd, headers, body)
    binary_list = []
    binary_list.append('['.encode(encoding="utf-8"))
    binary_list.append('"'.encode(encoding="utf-8"))
    binary_list.extend(convert_frame(frame))
    binary_list.append('"'.encode(encoding="utf-8"))
    binary_list.append(']'.encode(encoding="utf-8"))
    return pack(binary_list)





if __name__ =="__main__":
    result = send_frame(CMD_CONNECT,{
        "accept-version":"1.1",
        "heart-beat":"10000,10000"
    })
    print(result)
    print("\u0000")


