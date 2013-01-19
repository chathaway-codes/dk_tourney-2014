from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from tournament.models import Tournament, Game, Player, Computer, Team, TeamInvite
from tournament.forms import PlayerForm, ComputerForm, TeamForm, TeamInviteForm

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

@login_required
def tournament_reg(request, pk, **kwargs):
    tournament = get_object_or_404(Tournament, pk=pk)

    players = Player.objects.all()

    if request.user.tournament_set.filter(pk=tournament.id).count() == 0:
        request.user.tournament_set.add(tournament)
        return render_to_response('tournament/tournament_list.html', {"message":"You have been registered.", "list":Tournament.objects.all}, context_instance=RequestContext(request))
    else:
        request.user.tournament_set.remove(tournament)
        return render_to_response('tournament/tournament_list.html', {"message":"You have been unregistered.", "list":Tournament.objects.all}, context_instance=RequestContext(request))

class PlayerEditView(UpdateView):
    form_class = PlayerForm
    model = Player

class PlayerCreateView(CreateView):
    form_class = PlayerForm
    model = Player

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerCreateView, self).form_valid(form)

class ComputerEditView(UpdateView):
    form_class = ComputerForm
    model = Computer

class TeamListView(ListView):
    model = Team
    context_object_name = 'list'

class TeamDetailView(DetailView):
    model = Team
    context_object_name = 'team'

class TeamEditView(UpdateView):
    form_class = TeamForm
    model = Team

class TeamCreateView(CreateView):
    form_class = TeamForm
    model = Team

class TeamInviteCreateView(CreateView):
    form_class = TeamInviteForm
    model = TeamInvite

    def form_valid(self, form):
        form.instance.team = Team.objects.get(pk=self.kwargs['pk'])
        return super(TeamInviteCreateView, self).form_valid(form)
