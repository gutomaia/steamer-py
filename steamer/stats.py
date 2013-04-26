from lxml import objectify

import requests

def get_stats(username, game, xmlfile=None):

    if xmlfile != None:
        content = open(xmlfile).read()
    else:
        r = requests.get("http://localhost:8080/id/gutomaia/stats/tf2?xml=1")
        if r.status_code != 200:
            raise Exception
        content = r.content

    s = objectify.fromstring(content)

    stats = dict(
        visibilityState = 3,
        gameFriendlyName = s.game.gameFriendlyName,
        gameName =  s.game.gameName,
        gameLink = s.game.gameLink,
        gameIcon = s.game.gameIcon,
        gameLogo = s.game.gameLogo,
        gameLogoSmall = s.game.gameLogoSmall,
        steamID64 = 76561197985077150,
        playerCustomURL = 'gutomaia'
        )
    return stats

def get_achievements(username, game):
        pass