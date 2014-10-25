# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.views.generic import DetailView
from django.views.generic.dates import YearArchiveView, MonthArchiveView

from .models import ConsiglioComunaleEvent


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


class ConsiglioComunaleDetailView(DetailView):
    model = ConsiglioComunaleEvent