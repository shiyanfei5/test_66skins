

"""
http://www.mytju.com/classcode/tools/encode_utf8.asp
编码查看网站
"""


def bytes_to_hex_string(bs):
    return ''.join(['%02X ' % b for b in bs])


def str_to_hex_string(str_val, encoding):
    return bytes_to_hex_string(str_val.encode(encoding=encoding))


if __name__ == "__main__":
    print(bytes_to_hex_string(u"\u0000".encode("utf-8")))