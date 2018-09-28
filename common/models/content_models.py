from django.db import models
from django.utils.translation import ugettext_lazy as _


class WebContent(models.Model):
    key = models.CharField(max_length=64, db_index=True, unique=True, verbose_name=_('key'))
    text = models.TextField(null=True, blank=True, verbose_name=_('text'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('image'))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=_('date modified'))

    def __str__(self):
        return str(self.key)
