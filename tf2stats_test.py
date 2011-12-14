import unittest

from steamer.stats import StatsClient

class TF2StatsTest(unittest.TestCase):

    def setUp(self):
        stats_client = StatsClient()
        self.stats = stats_client.get_stats("gutomaia", "tf2") #TODO implement with document later on

    def tearDown(self):
        self.stats = None;

    def test_tf2_get_visibility_state(self):
        self.assertEquals(3, self.stats['visibilityState'])

    def test_tf2_get_game_friendly_name(self):
        self.assertEquals('TF2', self.stats['gameFriendlyName'])

    def test_tf2_get_game_name(self):
        self.assertEquals('Team Fortress 2', self.stats['gameName'])
    
    def test_tf2_get_game_link(self):
        self.assertEquals("http://store.steampowered.com/app/440", self.stats['gameLink']);