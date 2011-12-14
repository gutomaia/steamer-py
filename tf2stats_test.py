import unittest

from steamer.stats import get_stats

class TF2StatsTest(unittest.TestCase):

    def setUp(self):
        self.stats = get_stats("gutomaia", "tf2") #TODO implement with document later on

    def tearDown(self):
        self.stats = None;

    def test_tf2_get_visibility_state(self):
        self.assertEquals(3, self.stats['visibilityState'])

    def test_tf2_get_game_friendly_name(self):
        self.assertEquals('TF2', self.stats['gameFriendlyName'])

    def test_tf2_get_game_name(self):
        self.assertEquals('Team Fortress 2', self.stats['gameName'])
    
    def test_tf2_get_game_link(self):
        self.assertEquals('http://store.steampowered.com/app/440', self.stats['gameLink']);

    def test_tf2_get_game_icon(self):
        self.assertEquals('http://media.steampowered.com/steamcommunity/public/images/apps/440/e3f595a92552da3d664ad00277fad2107345f743.jpg', self.stats['gameIcon'])

    def test_tf2_get_game_logo(self):
        self.assertEquals('http://media.steampowered.com/steamcommunity/public/images/apps/440/07385eb55b5ba974aebbe74d3c99626bda7920b8.jpg', self.stats['gameLogo'])

    def test_tf2_get_game_logo_small(self):
        self.assertEquals('http://media.steampowered.com/steamcommunity/public/images/apps/440/07385eb55b5ba974aebbe74d3c99626bda7920b8_thumb.jpg', self.stats['gameLogoSmall'])

    def test_tf2_get_player_steam_id64(self):
        self.assertEquals(76561197985077150, self.stats['steamID64'])

    def test_tf2_get_player_custom_url(self):
        self.assertEquals('gutomaia', self.stats['playerCustomURL'])