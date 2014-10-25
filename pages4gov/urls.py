# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from datetime import date

from django.conf.urls import patterns, url

from .views import (ConsiglioComunaleYearArchiveView,
                    ConsiglioComunaleMonthArchiveView,
                    ConsiglioComunaleDetailView)


urlpatterns = patterns(
    'opa_trasparenza.views',
    url(r'^events/$', ConsiglioComunaleYearArchiveView.as_view(),
        name='events_list', kwargs={'year': str(date.today().year)}),
    url(r'^events/consigliocomunale/$',
        ConsiglioComunaleYearArchiveView.as_view(),
        name='consiglicomunali_current_archive',
        kwargs={'year': str(date.today().year)}),
    url(r'^events/consigliocomunale/(?P<year>\d{4})/$',
        ConsiglioComunaleYearArchiveView.as_view(),
        name='consiglicomunali_year_archive'),
    url(r'^events/consigliocomunale/(?P<year>\d{4})/(?P<month>\d+)/$',
        ConsiglioComunaleMonthArchiveView.as_view(month_format='%m'),
        name="consiglicomunali_month_archive"),
    url(r'^events/consigliocomunale/detail/(?P<pk>\d+)/$',
        ConsiglioComunaleDetailView.as_view(),
        name='consiglicomunali_detail'),
    # url(r'^opendata/avcp/l190/(?P<slug_ente>[-_\w]+)/datasetappalti/$',
    #     DatasetAppaltiListView.as_view(), name='datasetappalti_list'),
    # url(r'^opendata/avcp/l190/(?P<slug_ente>[-_\w]+)/datasetindice/$',
    #     DatasetIndiceListView.as_view(),
    #     name='datasetindice_list'),
    # url(r'^opendata/avcp/l190/(?P<slug_ente>[-_\w]+)/(?P<model>\w+)_(?P<year>\d{4})_(?P<pk>\d+)\.(?P<file_format>\w+)$',
    #     'dataset_export', name='dataset_export'),
)
