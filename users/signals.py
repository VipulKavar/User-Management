from Tools.demo.mcast import sender
from django.dispatch import receiver
from django.db.models.signals import post_save

from users.models import MyUser, Profile


@receiver(post_save, sender=MyUser)
def create_profile(instance, sender, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=MyUser)
def save_profile(instance, sender, **kwargs):
    instance.profile.save()