import unittest

from steamer.stats import StatsClient

class TF2StatsTest(unittest.TestCase):

    def setUp(self):
        stats_client = StatsClient()
        self.stats = stats_client.get_stats("gutomaia", "tf2") #TODO implement with document later on

    def tearDown(self):
        self.stats = None;

    def testOk(self):
        self.assertTrue(True)
