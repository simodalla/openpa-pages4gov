# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from copy import deepcopy

from django.contrib import admin
from django.utils.translation import ugettext as _
from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin

from .models import ConsiglioComunaleEvent
from .forms import ConsiglioComunaleEventForm


istitutionalevent_fieldsets = list(deepcopy(DisplayableAdmin.fieldsets))
istitutionalevent_fieldsets.insert(
    1, ('Multimedia', {'fields': ['performance_date',
                                  'news_url', 'youtube_video_url',
                                  'youtube_video_url_query', 'hangout_url',
                                  'content']}))
istitutionalevent_list_display = ['title', 'performance_date', 'user',
                                  'status', 'admin_link']
istitutionalevent_list_filter = deepcopy(DisplayableAdmin.list_filter)


class IstitutionalEventAdmin(DisplayableAdmin, OwnableAdmin):
    """
    Admin class for blog posts.
    """

    fieldsets = istitutionalevent_fieldsets
    list_display = istitutionalevent_list_display
    list_filter = istitutionalevent_list_filter
    date_hierarchy = 'performance_date'

    def save_form(self, request, form, change):
        """
        Super class ordering is important here - user must get saved first.
        """
        OwnableAdmin.save_form(self, request, form, change)
        return DisplayableAdmin.save_form(self, request, form, change)

    def save_model(self, request, obj, form, change):
        if obj.title == 'Consiglio Comunale':
            obj.title += ' del {:%d} {} {:%Y}'.format(
                obj.performance_date,
                _(obj.performance_date.strftime('%B')).capitalize(),
                obj.performance_date)
        obj.save()


class ConsiglioComunaleEventAdmin(IstitutionalEventAdmin):
    form = ConsiglioComunaleEventForm


admin.site.register(ConsiglioComunaleEvent, ConsiglioComunaleEventAdmin)