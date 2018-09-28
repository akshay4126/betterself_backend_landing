from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


class WebContent(models.Model):
    key = models.CharField(max_length=64, db_index=True, unique=True, verbose_name=_('key'))
    text = models.TextField(null=True, blank=True, verbose_name=_('text'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('image'))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=_('date modified'))

    class Meta:
        verbose_name = "Web content block"
        verbose_name_plural = "Web content blocks"

    def __str__(self):
        return str(self.key)


class WebContentEditor(models.Model):
    key = models.CharField(max_length=64, db_index=True, unique=True, verbose_name=_('key'))
    content = RichTextField(null=True, blank=True, verbose_name=_('content'))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=_('date modified'))

    class Meta:
        verbose_name = "Web content editor"
        verbose_name_plural = "Web content editor"

    def __str__(self):
        return str(self.key)
