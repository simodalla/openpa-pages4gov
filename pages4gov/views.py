# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.views.generic.list import ListView

from mezzanine.conf import settings

from .models import ConsiglioComunaleEvent


class SettingsMixin(object):

    context_app_settings = []

    def get_context_data(self, **kwargs):
        context = super(SettingsMixin, self).get_context_data(**kwargs)
        context.update({'app_settings': {}})
        settings.use_editable()
        for setting in self.context_app_settings:
            context['app_settings'].update(
                {setting.upper(): getattr(settings, setting, '')})
        return context


class EventiIstituzionaliHomeView(TemplateView):
    template_name = 'pages4gov/istitutionalevent_home.html'


class ConsiglioComunaleListView(ListView):
    model = ConsiglioComunaleEvent


class ConsiglioComunaleYearArchiveView(YearArchiveView):
    queryset = ConsiglioComunaleEvent.objects.published()
    date_field = 'performance_date'
    make_object_list = True
    allow_future = True
    allow_empty = True


class ConsiglioComunaleMonthArchiveView(MonthArchiveView):
    queryset = ConsiglioComunaleEvent.objects.published()
    date_field = 'performance_date'
    make_object_list = True
    allow_future = True
    allow_empty = True


class ConsiglioComunaleDetailView(SettingsMixin, DetailView):
    context_app_settings = ['PAGES4GOV_YOUTUBE_URL_QUERY',
                            'PAGES4GOV_YOUTUBE_EMBED_WIDTH',
                            'PAGES4GOV_YOUTUBE_EMBED_HEIGHT']
    model = ConsiglioComunaleEvent

