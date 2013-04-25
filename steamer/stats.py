
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

    if game == 'portal2':
        from lxml import objectify
        content = open(xmlfile).read()
        s = objectify.fromstring(content)
        stats['gameFriendlyName'] = s.game.gameFriendlyName
        stats['gameName'] = s.game.gameName
        stats['gameLink'] = s.game.gameLink
        stats['gameIcon'] = s.game.gameIcon
        stats['gameLogo'] = s.game.gameLogo
        stats['gameLogoSmall'] = s.game.gameLogoSmall
    elif game == 'l4d2':
        stats['gameFriendlyName'] = 'L4D2'
        stats['gameName'] = 'Left 4 Dead 2'
        stats['gameLink'] = 'http://store.steampowered.com/app/550'
        stats['gameIcon'] = 'http://media.steampowered.com/steamcommunity/public/images/apps/550/7d5a243f9500d2f8467312822f8af2a2928777ed.jpg'
        stats['gameLogo'] = 'http://media.steampowered.com/steamcommunity/public/images/apps/550/205863cc21e751a576d6fff851984b3170684142.jpg'
        stats['gameLogoSmall'] = 'http://media.steampowered.com/steamcommunity/public/images/apps/550/205863cc21e751a576d6fff851984b3170684142_thumb.jpg'
    return stats

def get_achievements(username, game):
        pass