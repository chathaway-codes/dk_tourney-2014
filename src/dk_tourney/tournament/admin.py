from django.contrib import admin

from tournament.models import Game, Team, Tournament, Player

admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Player)
