from django.db.models.signals import post_save
from django.dispatch import receiver

from blackboards.models import Board


@receiver(post_save, sender=Board)
def update_stock(sender, **kwargs):
    kwargs['raw'] = True
    instance = kwargs.get("instance")
    if len(instance.users.all()) == 0:
        instance.users.add(instance.owner.pk)
        instance.save()
    test = instance.users.all()
    test = instance.users.all()
