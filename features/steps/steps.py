from behave import *
from steamer.stats import get_stats
from tests.integration.steam_simulator import SteamSimulator


@given(r'gutomaia as user')
def impl(context):
    context.username = 'gutomaia'

@when(u'he asks for the tf2 status')
def impl(context):
    context.game = 'tf2'
    context.stas = get_stats(context.username, context.game)


@then(u'the gameName is Team Fortress 2')
def impl(context):
	pass