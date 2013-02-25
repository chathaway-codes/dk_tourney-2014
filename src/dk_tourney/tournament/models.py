from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class File(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    file = models.FileField(upload_to="file/%Y-%m-%d %H:%M:%S-")

    def __unicode__(self):
        return self.name

class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    description = models.TextField(help_text="Put some information about yourself here. This will be visible to the world", null=True, blank=True)

    image = models.ImageField(help_text="Make it unique and memorable!", upload_to="players/%Y-%m-%d %H:%M:%S-", null=True, blank=True)

    handle = models.CharField(max_length=255, help_text="This is an alias for yourself. This will appear everywhere instead of your username", null=True, blank=True)
    games = models.ManyToManyField('Game', help_text="Please select the games you would like to play", null=True, blank=True)
    platforms = models.ManyToManyField('Platform', help_text="Please select a few platforms you own", null=True, blank=True)

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
    player = models.OneToOneField('Player')

    cpu = models.CharField(max_length=255, null=True, blank=True)
    gpu = models.CharField(max_length=255, null=True, blank=True)
    ram = models.CharField(max_length=255, null=True, blank=True)
    hdd = models.CharField(max_length=255, null=True, blank=True)
    wat = models.PositiveIntegerField(verbose_name="Power Supply Wattage", null=True, blank=True)

    other = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('player_detail', kwargs={'pk': self.player.pk})

class TeamInvite(models.Model):
    team = models.ForeignKey('Team')
    player = models.ForeignKey('Player')

    when = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.team.name + " invites " + self.player.get_name()

    def get_absolute_url(self):
        return reverse('team_detail', kwargs={'pk': self.team.id})

class Team(models.Model):
    name = models.CharField(max_length=255)

    lead = models.ForeignKey('Player', related_name="team_lead_set")

    members = models.ManyToManyField('Player', through='TeamInvite')
    tournaments = models.ManyToManyField('Tournament', blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team_detail', kwargs={'pk': self.id})

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    game = models.ForeignKey('Game')
    team_size = models.IntegerField(default=1)

    def get_name(self):
        return self.game.name + ' -- ' + self.name

    def __unicode__(self):
        return self.get_name()

# Place holder to make messages work
class Message(models.Model):
    message = models.CharField(max_length=4096)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

# Include the signals
import tournament.signals
