from steamer.stats import get_stats, get_achievements

from portal2_test import Portal2StatsTest

from integration.steam_simulator import SteamSimulator

class Portal2StatsIntegrationTest(Portal2StatsTest):

    @classmethod
    def setUpClass(cls):
        cls.sim = SteamSimulator()
        cls.sim.start()
        cls.stats = get_stats("gutomaia", "portal2")

    @classmethod
    def tearDownClass(cls):
        cls.stats = None;
        cls.sim.stop()
        while not cls.sim.stopped():
            sleep(0.1)

if __name__ == '__main__':
    unittest.main()
