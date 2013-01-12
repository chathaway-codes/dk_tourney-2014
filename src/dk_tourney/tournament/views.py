from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from tournament.models import Tournament

class TournamentListView(ListView):
    model = Tournament
    context_object_name = 'list'

class TournamentDetailedView(DetailView):
    model = Tournament
    context_object_name = 'tourney'
