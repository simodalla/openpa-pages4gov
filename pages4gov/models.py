# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from future.builtins import str

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import Displayable, Ownable, RichText, Slugged


class IstitutionalEvent(Displayable, Ownable, RichText):

    performance_date = models.DateTimeField(
        verbose_name=_('Data di svolgimento'))
    news_url = models.URLField(verbose_name=_('Url della notizia'),
                               blank=True)
    youtube_video_url = models.URLField(verbose_name=_('Url di YouTube'),
                                        blank=True)
    youtube_video_url_query = models.CharField(verbose_name=_("Query dell'url"
                                                              " di YouTube"),
                                               max_length=200, blank=True)
    hangout_url = models.URLField(verbose_name=_("Url dell'hangout"),
                                  blank=True)

    class Meta:
        abstract = True
        ordering = ("-performance_date",)


class ConsiglioComunaleEvent(IstitutionalEvent):
    """
    A IstitutionalEvent of type ConsiglioComunale.
    """

    class Meta:
        verbose_name = _("Consiglio Comunale")
        verbose_name_plural = _("Consigli Comunali")

    def get_absolute_url(self):
        return '/{}/'.format(self.pk)
