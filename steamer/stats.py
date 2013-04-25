
def get_stats(username, game, xmlfile=None):
    stats = dict(
        visibilityState = 3,
        gameFriendlyName = 'TF2',
        gameName = 'Team Fortress 2',
        gameLink = 'http://store.steampowered.com/app/440',
        gameIcon = 'http://media.steampowered.com/steamcommunity/public/images/apps/440/e3f595a92552da3d664ad00277fad2107345f743.jpg',
        gameLogo = 'http://media.steampowered.com/steamcommunity/public/images/apps/440/07385eb55b5ba974aebbe74d3c99626bda7920b8.jpg',
        gameLogoSmall = 'http://media.steampowered.com/steamcommunity/public/images/apps/440/07385eb55b5ba974aebbe74d3c99626bda7920b8_thumb.jpg',
        steamID64 = 76561197985077150,
        playerCustomURL = 'gutomaia'
        )

    if game == 'portal2' or game == 'l4d2':
        from lxml import objectify
        content = open(xmlfile).read()
        s = objectify.fromstring(content)
        stats['gameFriendlyName'] = s.game.gameFriendlyName
        stats['gameName'] = s.game.gameName
        stats['gameLink'] = s.game.gameLink
        stats['gameIcon'] = s.game.gameIcon
        stats['gameLogo'] = s.game.gameLogo
        stats['gameLogoSmall'] = s.game.gameLogoSmall
    return stats

def get_achievements(username, game):
        pass