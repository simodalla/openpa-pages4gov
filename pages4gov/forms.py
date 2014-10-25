# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django import forms

from .models import ConsiglioComunaleEvent


class ConsiglioComunaleEventForm(forms.ModelForm):
    """
    Model form for ``BlogPost`` that provides the quick blog panel in the
    admin dashboard.
    """

    class Meta:
        model = ConsiglioComunaleEvent

    def __init__(self, *args, **kwargs):
        super(ConsiglioComunaleEventForm, self).__init__(*args, **kwargs)
        self.fields['title'].initial = 'Consiglio Comunale'
