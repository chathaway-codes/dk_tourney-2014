from tournament.models import Team, TeamInvite

from django import template

register = template.Library()

def get_team_members(team):
    return team.members.filter(teaminvite__accepted=True)

def get_player_team(tournament, player):
    return player.team_set.filter(tournaments=tournament, teaminvite__accepted=True)

register.filter('get_team_members', get_team_members)

register.filter('get_player_team', get_player_team)
