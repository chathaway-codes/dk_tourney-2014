from django.db import models

from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User)

    handle = models.CharField(max_length=255, null=True, blank=True)

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4096)

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)

    members = models.ManyToManyField(User)
    tournaments = models.ManyToManyField('Tournament')

    def __unicode__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4096)

    game = models.ForeignKey('Game')
    team_game = models.BooleanField()
    team_size = models.IntegerField(null=True, blank=True)

    players = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return self.game.name + ' -- ' + self.name

