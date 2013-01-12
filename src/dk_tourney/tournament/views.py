from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User

from tournament.models import Tournament, Game

class TournamentListView(ListView):
    model = Tournament
    context_object_name = 'list'

class TournamentDetailedView(DetailView):
    model = Tournament
    context_object_name = 'list'


class GameListView(ListView):
    model = Game
    context_object_name = 'list'

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'


@login_required
def interest_in_game(request, pk, **kwargs):
    game = get_object_or_404(Game, pk=pk)

    if game not in request.user.player.games.all():
        request.user.player.games.add(game)
    
    return render_to_response('tournament/game_interest_added.html', {"game": game}, context_instance=RequestContext(request))
