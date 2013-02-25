from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User

from guardian.mixins import PermissionRequiredMixin

from tournament.models import Tournament, Game, Player, Computer, Team, TeamInvite
from tournament.forms import PlayerForm, ComputerForm, TeamForm, TeamInviteForm, TeamInviteAcceptForm


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
def interest_in_tournament(request, pk, **kwargs):
    tournament = get_object_or_404(Tournament, pk=pk)

    if tournament.team_size != 1:
        raise Http404

    if tournament.team_set.filter(lead=request.user.player).count() == 0:
        t = Team(name=request.user.player.get_name() + " for " + tournament.__unicode__(), lead=request.user.player)
        t.save()
        t.tournaments.add(tournament)
        tournaments = Tournament.objects.all()
        return render_to_response('tournament/tournament_list.html', {"message":"Your interest has been noted!", "list":tournaments}, context_instance=RequestContext(request))
    else:
        t = request.user.player.team_lead_set.filter(tournaments=tournament)
        t[0].delete()
        tournaments = Tournament.objects.all()
        return render_to_response('tournament/tournament_list.html', {"message":"Your lock of interest has been noted!", "list":tournaments}, context_instance=RequestContext(request))

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

class PlayerEditView(PermissionRequiredMixin, UpdateView):
    form_class = PlayerForm
    model = Player

    permission_required = "tournament.change_player"
    return_403 = True

    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        return super(PlayerEditView, self).dispatch(request, *args, **kwargs)

class PlayerCreateView(CreateView):
    form_class = PlayerForm
    model = Player

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerCreateView, self).form_valid(form)

class ComputerEditView(PermissionRequiredMixin, UpdateView):
    form_class = ComputerForm
    model = Computer

    permission_required = "tournament.change_computer"
    return_403 = True

    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        return super(ComputerEditView, self).dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
      self.kwargs = kwargs
      self.request = request
      return super(TeamCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
      form.instance.lead = self.request.user.player
      return super(TeamCreateView, self).form_valid(form)

class TeamInviteCreateView(PermissionRequiredMixin, CreateView):
    form_class = TeamInviteForm
    model = TeamInvite
    template_name = 'tournament/teaminvite_create.html'

    permission_required = "tournament.create_teaminvite"
    return_403 = True

    def check_permissions(self, request):
        team = Team.objects.get(pk=self.kwargs['pk'])
        if request.user.player == team.lead:
            return None
        raise PermissionDenied()

    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        return super(TeamInviteCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.team = Team.objects.get(pk=self.kwargs['pk'])
        return super(TeamInviteCreateView, self).form_valid(form)

class TeamInviteEditView(PermissionRequiredMixin, UpdateView):
    form_class = TeamInviteAcceptForm
    model = TeamInvite

    permission_required = "tournament.create_teaminvite"
    return_403 = True

    def get_object(self):
        # Just in case they do anything funky... Ie, check_permissions
        super(TeamInviteEditView, self).get_object()
        team = Team.objects.get(pk=self.kwargs['pk'])
        return TeamInvite.objects.filter(team=team, player=self.request.user.player)[0]

    def check_permissions(self, request):
        team = Team.objects.get(pk=self.kwargs['pk'])
        team_invite = TeamInvite.objects.filter(team=team, player=request.user.player)
        if team_invite.count > 0:
            self.request = request
            return None
        raise PermissionDenied()

    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        return super(TeamInviteEditView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.team = Team.objects.get(pk=self.kwargs['pk'])
        return super(TeamInviteEditView, self).form_valid(form)

