import unittest

from steamer.stats import get_stats

class Portal2StatsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stats = get_stats("gutomaia", "portal2", 'fixtures/gutomaia-portal2.xml')

    @classmethod
    def tearDownClass(cls):
        cls.stats = None

    def test_portal2_get_visibility_state(self):
        self.assertEquals(3, self.stats['visibilityState'])

    def test_portal2_get_game_friendly_name(self):
        self.assertEquals('Portal2', self.stats['gameFriendlyName'])
    
    def test_portal2_get_game_name(self):
        self.assertEquals('Portal 2', self.stats['gameName'])
    
    def test_portal2_get_game_link(self):
        self.assertEquals('http://store.steampowered.com/app/620', self.stats['gameLink'])

    def test_portal2_get_game_icon(self):
        self.assertEquals('http://media.steampowered.com/steamcommunity/public/images/apps/620/2e478fc6874d06ae5baf0d147f6f21203291aa02.jpg', self.stats['gameIcon'])

    def test_portal2_get_game_logo(self):
        self.assertEquals('http://media.steampowered.com/steamcommunity/public/images/apps/620/d2a1119ddc202fab81d9b87048f495cbd6377502.jpg', self.stats['gameLogo'])

    def test_portal2_get_game_logo_small(self):
        self.assertEquals('http://media.steampowered.com/steamcommunity/public/images/apps/620/d2a1119ddc202fab81d9b87048f495cbd6377502_thumb.jpg', self.stats['gameLogoSmall'])

    def test_portal2_get_player_steam_id64(self):
        self.assertEquals(76561197985077150, self.stats['steamID64'])

    def test_portal2_get_player_custom_url(self):
        self.assertEquals('gutomaia', self.stats['playerCustomURL'])

if __name__ == '__main__':
    unittest.main()
