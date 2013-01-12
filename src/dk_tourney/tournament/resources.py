from tastypie.resources import ModelResource
from tastypie.constants import ALL
from rest_api.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization

from tournament.models import Player, Tournament, Game, Computer, Platform, Team

class PlayerResource(ModelResource):
    class Meta:
        queryset = Player.objects.all()
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            'id': ALL,
        }

class TournamentResource(ModelResource):
    class Meta:
        queryset = Tournament.objects.all()
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            'id': ALL,
        }

class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            'id': ALL,
        }

class ComputerResource(ModelResource):
    class Meta:
        queryset = Computer.objects.all()
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            'id': ALL,
        }

class PlatformResource(ModelResource):
    class Meta:
        queryset = Platform.objects.all()
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            'id': ALL,
        }

class TeamResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            'id': ALL,
        }

