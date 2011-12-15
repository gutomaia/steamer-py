
def get_stats(username, game):
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
        stats['gameFriendlyName'] = 'Portal2'
        stats['gameName'] = 'Portal 2'
        stats['gameLink'] = 'http://store.steampowered.com/app/620'
        stats['gameIcon'] = 'http://media.steampowered.com/steamcommunity/public/images/apps/620/2e478fc6874d06ae5baf0d147f6f21203291aa02.jpg'
        stats['gameLogo'] = 'http://media.steampowered.com/steamcommunity/public/images/apps/620/d2a1119ddc202fab81d9b87048f495cbd6377502.jpg'
        stats['gameLogoSmall'] = 'http://media.steampowered.com/steamcommunity/public/images/apps/620/d2a1119ddc202fab81d9b87048f495cbd6377502_thumb.jpg'
    elif game == 'l4d2':
        stats['gameFriendlyName'] = 'L4D2'
        stats['gameName'] = 'Left 4 Dead 2'
        stats['gameLink'] = 'http://store.steampowered.com/app/550'
        stats['gameIcon'] = 'http://media.steampowered.com/steamcommunity/public/images/apps/550/7d5a243f9500d2f8467312822f8af2a2928777ed.jpg'
        stats['gameLogo'] = 'http://media.steampowered.com/steamcommunity/public/images/apps/550/205863cc21e751a576d6fff851984b3170684142.jpg'
    return stats
