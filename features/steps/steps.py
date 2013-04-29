from behave import *
from behave.matchers import register_type

from steamer.stats import get_stats
from tests.integration.steam_simulator import SteamSimulator

from behave.matchers import register_type
register_type(username=lambda s: s)
register_type(string=lambda s: s)

@given(r'{username:username} as user')
def impl(context, username):
    context.username = username

@when(u'he asks for the {game:string} status')
def impl(context, game):
    context.game = game
    context.stats = get_stats(context.username, context.game)

@then(u'the {key:string} is {value:string}')
def impl(context, key, value):
	assert context.stats[key] == value, 'The %s should be %s and it is %s' % (key, value, context.stats[key])