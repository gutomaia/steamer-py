import threading
from time import sleep

import web
import requests


urls = (
    '/(.*)', 'ok_page'
)

class ok_page(object):
    def GET(self, request):               
        return "ok"


class SteamSimulator(threading.Thread):
    def __init__(self):
        super(SteamSimulator, self).__init__()
        self._stop = threading.Event()

    def run(self):
        self.app = web.application(urls, globals())
        web.config.default_port = 8080
        self.app.internalerror = web.debugerror
        self.app.run()

    def stop(self):
        self.join(3)
        self.app.stop()
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()