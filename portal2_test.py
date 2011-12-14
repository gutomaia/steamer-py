import unittest

from steamer.stats import get_stats

class Portal2StatsTest(unittest.TestCase):

    def setUp(self):
        self.stats = get_stats("gutomaia", "portal2") #TODO implement with document later on

    def tearDown(self):
        self.stats = None;

    def test_portal2_get_visibility_state(self):
        self.assertEquals(3, self.stats['visibilityState'])
