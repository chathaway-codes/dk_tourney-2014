from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User

from tournament.models import Tournament, Game, Player

class TournamentListView(ListView):
    model = Tournament
    context_object_name = 'list'

class TournamentDetailView(DetailView):
    model = Tournament
    context_object_name = 'tourney'


class GameListView(ListView):
    model = Game
    context_object_name = 'list'

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'

class PlayerListView(ListView):
    model = Player
    context_object_name = 'list'

class PlayerDetailView(DetailView):
    model = Player
    context_object_name = 'player'

@login_required
def interest_in_game(request, pk, **kwargs):
    game = get_object_or_404(Game, pk=pk)

    games = Game.objects.all()

    if game not in request.user.player.games.all():
        request.user.player.games.add(game)
        return render_to_response('tournament/game_list.html', {"message":"Your interest has been noted!", "list":games}, context_instance=RequestContext(request))
    else:
        request.user.player.games.remove(game)
        return render_to_response('tournament/game_list.html', {"message":"Your lack of interest has been noted!", "list":games}, context_instance=RequestContext(request))
