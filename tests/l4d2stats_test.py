import unittest

from steamer.stats import get_stats, get_achievements

class L4D2StatsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stats = get_stats("gutomaia", "l4d2", 'fixtures/gutomaia-l4d2.xml')

    @classmethod
    def tearDownClass(cls):
        cls.stats = None

    def test_l4d2_get_visibility_state(self):
        self.assertEquals(3, self.stats['visibilityState'])

    def test_l4d2_get_game_friendly_name(self):
        self.assertEquals('L4D2', self.stats['gameFriendlyName'])

    def test_l4d2_get_game_name(self):
        self.assertEquals('Left 4 Dead 2', self.stats['gameName'])

    def test_l4d2_get_game_link(self):
        self.assertEquals('http://store.steampowered.com/app/550', self.stats['gameLink'])

    def test_l4d2_get_game_icon(self):
        self.assertEquals('http://media.steampowered.com/steamcommunity/public/images/apps/550/7d5a243f9500d2f8467312822f8af2a2928777ed.jpg', self.stats['gameIcon'])

    def test_l4d2_get_game_logo(self):
        self.assertEquals('http://media.steampowered.com/steamcommunity/public/images/apps/550/205863cc21e751a576d6fff851984b3170684142.jpg', self.stats['gameLogo'])

    def test_l4d2_get_game_logo_small(self):
        self.assertEquals('http://media.steampowered.com/steamcommunity/public/images/apps/550/205863cc21e751a576d6fff851984b3170684142_thumb.jpg', self.stats['gameLogoSmall'])

    def test_l4d2_get_player_steam_id64(self):
        self.assertEquals(76561197985077150, self.stats['steamID64'])

    def test_l4d2_get_player_custom_url(self):
        self.assertEquals('gutomaia', self.stats['playerCustomURL'])

    def test_get_achievements(self):
        achievements = get_achievements("gutomaia", "L4D2")

if __name__ == '__main__':
    unittest.main()
