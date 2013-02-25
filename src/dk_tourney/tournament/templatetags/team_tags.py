from tournament.models import Team, TeamInvite

from django import template

register = template.Library()

def get_team_members(team):
    return team.members.filter(teaminvite__accepted=True)

def get_player_team(tournament, player):
    return player.team_set.filter(tournaments=tournament, teaminvite__accepted=True)

def get_tournament_players(tournament):
    teams = tournament.team_set.all()
    team_size = tournament.team_size
    players = []
    for t in teams:
        if team_size == 1:
            players += [t.lead]
        else:
            players += list(t.members.all())
    return players

def player_registered(tournament, player):
    if player.team_set.filter(tournaments=tournament, teaminvite__accepted=True).count() == 1:
        return True
    if player.team_lead_set.filter(tournaments=tournament).count() == 1:
        return True
    return False

register.filter('get_team_members', get_team_members)

register.filter('get_player_team', get_player_team)

register.filter('get_tournament_players', get_tournament_players)

register.filter('player_registered', player_registered)
