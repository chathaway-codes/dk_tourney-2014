from tournament.models import Team, TeamInvite

from django import template

register = template.Library()

def get_team_members(team):
    return team.members.filter(teaminvite__accepted=True)

register.filter('get_team_members', get_team_members)

