from django.db.models.signals import post_save

from user.models import SubscribeList
from user.tasks import new_subscribe_list_mail


# noinspection PyUnusedLocal
def subscribe_list_post_save(sender, instance, **kwargs):
    if not kwargs['created']:
        return
    new_subscribe_list_mail.delay([instance.email])


post_save.connect(subscribe_list_post_save, sender=SubscribeList)
