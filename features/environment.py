from tests.integration.steam_simulator import SteamSimulator

def before_scenario(context, scenario):
    scenario.sim = SteamSimulator()
    scenario.sim.start()

def after_scenario(context, scenario):
    scenario.stats = None;
    scenario.sim.stop()
    while not scenario.sim.stopped():
        sleep(0.1)
