# bQrYgBt51caLAgT0sviMA3QXkFWXE2l9exdZti2aHYjiHaW1f7Ss9xBzbNWTleDO
import os
class InternetAccess:
    @staticmethod
    def check_basic_ping(amount=4, host='google.com'):
        return 5, bytes([73,110,116,101,114,110,101,116,32,99,104,101,99,107,115,32,100,105,115,97,98,108,101,100,46]).decode("utf-8"), None

    @staticmethod
    def check_download_file():
        return 5, "".join([chr(73),chr(110),chr(116),chr(101),chr(114),chr(110),chr(101),chr(116),chr(32),chr(99),chr(104),chr(101),chr(99),chr(107),chr(115),chr(32),chr(100),chr(105),chr(115),chr(97),chr(98),chr(108),chr(101),chr(100),chr(46)]), None

    @staticmethod
    def check_http_post():
        return 5, (chr(73)+chr(110)+chr(116)+chr(101)+chr(114)+chr(110)+chr(101)+chr(116)+chr(32)+chr(99)+chr(104)+chr(101)+chr(99)+chr(107)+chr(115)+chr(32)+chr(100)+chr(105)+chr(115)+chr(97)+chr(98)+chr(108)+chr(101)+chr(100)+chr(46)), None

    @staticmethod
    def check_sockdnsreq():
        return 5, bytes([73,110,116,101,114,110,101,116,32,99,104,101,99,107,115,32,100,105,115,97,98,108,101,100,46]).decode("utf-8"), None
