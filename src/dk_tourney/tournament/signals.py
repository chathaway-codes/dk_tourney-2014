from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission

from guardian.shortcuts import assign

from tournament.models import Player, Computer

@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    if created and instance.username != 'AnonymousUser':
        p = Player(user=instance)
        p.save()
        Computer(player=p).save()

        assign('change_player', p.user, p)
        assign('change_computer', p.user, p.computer)
    
