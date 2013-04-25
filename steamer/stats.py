from lxml import objectify

def get_stats(username, game, xmlfile=None):
    content = open(xmlfile).read()
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