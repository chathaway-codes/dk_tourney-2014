from django.db import models
from django.core.urlresolvers import reverse


from django.contrib.auth.models import User

class File(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    file = models.FileField(upload_to="file/%Y-%m-%d %H:%M:%S-")

    def __unicode__(self):
        return self.name

class Player(models.Model):
    user = models.OneToOneField(User)
    description = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to="players/%Y-%m-%d %H:%M:%S-", null=True, blank=True)

    handle = models.CharField(max_length=255, null=True, blank=True)
    games = models.ManyToManyField('Game', blank=True)
    platforms = models.ManyToManyField('Platform', blank=True)

    def get_name(self):
        if self.handle != None and self.handle != "":
            return self.handle
        return self.user.username

    def __unicode__(self):
        return self.get_name()

    def get_absolute_url(self):
        return reverse('player_detail', kwargs={'pk': self.pk})

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="games/%Y-%m-%d %H:%M:%S-", null=True, blank=True)

    files = models.ManyToManyField('File', blank=True)

    platforms = models.ForeignKey('Platform')

    def __unicode__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Computer(models.Model):
    models.ForeignKey(Player)

    cpu = models.CharField(max_length=255, null=True, blank=True)
    gpu = models.CharField(max_length=255, null=True, blank=True)
    ram = models.CharField(max_length=255, null=True, blank=True)
    hdd = models.CharField(max_length=255, null=True, blank=True)
    wat = models.PositiveIntegerField(null=True, blank=True)

    other = models.TextField(null=True, blank=True)

class Team(models.Model):
    name = models.CharField(max_length=255)

    members = models.ManyToManyField(Player)
    tournaments = models.ManyToManyField('Tournament', blank=True)

    def __unicode__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    game = models.ForeignKey('Game')
    team_game = models.BooleanField()
    team_size = models.IntegerField(null=True, blank=True)

    players = models.ManyToManyField(Player, blank=True)

    def get_name(self):
        return self.game.name + ' -- ' + self.name

    def __unicode__(self):
        return self.get_name()

# Include the signals
import tournament.signals
