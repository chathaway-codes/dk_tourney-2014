from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm

from tournament.models import Game, Tournament, Player

def home(request):
    games = Game.objects.all()
    total_games = Game.objects.all().count()
    total_tournaments = Tournament.objects.all().count()
    total_players = Player.objects.all().count()

    return render_to_response('home.html', {"games": games, "form": AuthenticationForm(), "total_players": total_players, "total_games": total_games, "total_tournaments": total_tournaments}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))
