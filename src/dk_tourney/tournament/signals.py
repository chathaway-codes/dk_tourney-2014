from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from guardian.shortcuts import assign

from tournament.models import Player, Computer

@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    if created:
        p = Player(user=instance)
        p.save()

        assign('edit', instance, p)

        Computer(player=p).save()
    
