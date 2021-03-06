from steamer.stats import get_stats, get_achievements

from portal2_test import Portal2StatsTest

from integration.steam_simulator import SteamSimulator

import mock

class Portal2StatsMockedTest(Portal2StatsTest):

    @classmethod
    def setUpClass(cls):
        cls.patcher = mock.patch('steamer.stats.requests')
        requests_mocked = cls.patcher.start()
        content = open('fixtures/gutomaia-portal2.xml').read()
        response = mock.Mock()
        response.content = content
        response.status_code = 200
        requests_mocked.get.return_value = response
        cls.stats = get_stats("gutomaia", "portal2")

    @classmethod
    def tearDownClass(cls):
        cls.patcher.stop()
        cls.stats = None

if __name__ == '__main__':
    unittest.main()
