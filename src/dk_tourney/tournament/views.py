from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from tournament.models import Tournament, Game

class TournamentListView(ListView):
    model = Tournament
    context_object_name = 'list'

class TournamentDetailedView(DetailView):
    model = Tournament
<<<<<<< HEAD
    context_object_name = 'tourney'
=======
    context_object_name = 'list'


class GameListView(ListView):
    model = Game
    context_object_name = 'list'

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'
>>>>>>> 3728d383093bf0e19251d6dfb19bf64d6f2576c5
