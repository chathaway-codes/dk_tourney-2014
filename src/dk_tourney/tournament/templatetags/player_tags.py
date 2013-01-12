from tournament.models import Player

from django import template

register = template.Library()

def get_registered_tournaments(user):
    tourneys = user.tournament_set.all()
    for team in user.team_set.all():
        tourneys += team.tournaments.all()
        
    return tourneys


def get_registered_tournaments_count(user):
    return len(get_registered_tournaments(user))

register.filter('get_registered_tournaments_count', get_registered_tournaments_count)
