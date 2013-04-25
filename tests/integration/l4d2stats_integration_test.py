from steamer.stats import get_stats, get_achievements

from l4d2stats_test import L4D2StatsTest

from integration.steam_simulator import SteamSimulator

class L4D2StatsIntegrationTest(L4D2StatsTest):

    @classmethod
    def setUpClass(cls):
        cls.sim = SteamSimulator()
        cls.sim.start()
        cls.stats = get_stats("gutomaia", "l4d2", 'fixtures/gutomaia-l4d2.xml')
    
    @classmethod
    def tearDownClass(cls):
        cls.stats = None;
        cls.sim.stop()
        #while not cls.sim.stopped():
        #    sleep(0.1)

if __name__ == '__main__':
    unittest.main()
