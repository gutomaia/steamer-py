from steamer.stats import get_stats, get_achievements

from tf2stats_test import TF2StatsTest

from integration.steam_simulator import SteamSimulator

class TF2StatsIntegrationTest(TF2StatsTest):

    @classmethod
    def setUpClass(cls):
        cls.sim = SteamSimulator()
        cls.sim.start()
        cls.stats = get_stats("gutomaia", "tf2")

    @classmethod
    def tearDownClass(cls):
        cls.stats = None;
        cls.sim.stop()
        while not cls.sim.stopped():
            sleep(0.1)

if __name__ == '__main__':
    unittest.main()
