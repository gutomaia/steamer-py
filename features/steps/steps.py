from behave import *
from steamer.stats import get_stats
from tests.integration.steam_simulator import SteamSimulator


@given(r'gutomaia as user')
def impl(context):
    context.username = 'gutomaia'

@when(u'he asks for the tf2 status')
def impl(context):
    context.game = 'tf2'
    context.stats = get_stats(context.username, context.game)

@then(u'the gameName is Team Fortress 2')
def impl(context):
	assert context.stats['gameName'] == 'Team Fortress 2'

@then(u'the gameFriendlyName is TF2')
def impl(context):
	assert context.stats['gameFriendlyName'] == 'TF2'
