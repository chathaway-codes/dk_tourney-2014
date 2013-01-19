from tournament.models import Player, Team, TeamInvite

from django import template

register = template.Library()

def get_registered_tournaments(user):
    t = TeamInvite.objects.filter(player=user, accepted=True)
    tourneys = []
    for c in t:
        tourneys += list(c.team.tournaments.all())
    seen = set()
    seen_add = seen.add
    return [ x for x in tourneys if x not in seen and not seen_add(x) ]


def get_registered_tournaments_count(user):
    return len(get_registered_tournaments(user))

def get_teams(user):
    t = TeamInvite.objects.filter(player=user, accepted=True)
    teams = []
    for c in t:
        teams += [c.team]
    return teams

def get_pending_teams(user):
    t = TeamInvite.objects.filter(player=user, accepted=False)
    teams = []
    for c in t:
        teams += [c.team]
    return teams

register.filter('get_registered_tournaments', get_registered_tournaments)
register.filter('get_registered_tournaments_count', get_registered_tournaments_count)
register.filter('get_teams', get_teams)
register.filter('get_pending_teams', get_pending_teams)
