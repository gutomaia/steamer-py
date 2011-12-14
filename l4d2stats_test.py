import unittest

from steamer.stats import get_stats

class L4D2StatsTest(unittest.TestCase):

    def setUp(self):
        self.stats = get_stats("gutomaia", "l4d2") #TODO implement with document later on

    def tearDown(self):
        self.stats = None;

    def test_l4d2_get_visibility_state(self):
        self.assertEquals(3, self.stats['visibilityState'])