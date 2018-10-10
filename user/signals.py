from django.db.models.signals import post_save

from user.models import SubscribeList, ContactForm
from user.tasks import new_subscribe_list_mail, contact_us_admin_mail


# noinspection PyUnusedLocal
def subscribe_list_post_save(sender, instance, **kwargs):
    if not kwargs['created']:
        return
    new_subscribe_list_mail.delay([instance.email])


# noinspection PyUnusedLocal
def contact_form_post_save(sender, instance, **kwargs):
    if not kwargs['created']:
        return
    contact_us_admin_mail.delay(instance.pk)


post_save.connect(subscribe_list_post_save, sender=SubscribeList)
post_save.connect(contact_form_post_save, sender=ContactForm)
