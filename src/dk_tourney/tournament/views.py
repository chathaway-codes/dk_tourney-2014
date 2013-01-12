from django.http import HttpResponse
from django.views.generic import ListView

from tournament.models import Tournament

class TournamentListView(ListView):
    model = Tournament
    context_object_name = 'list'
