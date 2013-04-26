import threading
from time import sleep

import web
import requests


urls = (
    '/id/(\w+)/stats/(\w+)', 'game_page'
)

class game_page(object):
    def GET(self, user, game):
        f = open('fixtures/%s-%s.xml' % (user, game))
        xml = f.read()
        f.close()
        web.header('Content-Length', len(xml))
        return xml


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

if __name__ == "__main__":
    sim = SteamSimulator()
    sim.run()