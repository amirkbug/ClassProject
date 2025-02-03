<<<<<<< HEAD
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, Profile



@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
=======

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User , Profile


@receiver(post_save , sender=User)
def create_user_profile(instance , created , **kwargs):
>>>>>>> 9ae4125d25837591c830acf2775889779af1a937
    if created:
        Profile.objects.create(user=instance)