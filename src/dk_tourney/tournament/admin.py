from django.contrib import admin

from tournament.models import Game, Team, TeamInvite, Tournament, Player, Platform, File, Computer

admin.site.register(Game)
admin.site.register(Team)
admin.site.register(TeamInvite)
admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(Platform)
admin.site.register(File)
admin.site.register(Computer)
