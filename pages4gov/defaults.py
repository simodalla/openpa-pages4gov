# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from mezzanine.conf import register_setting


register_setting(
    name="PAGES4GOV_YOUTUBE_URL_QUERY",
    description="Specifica i parametri per la URL di YouTube.",
    editable=True,
    default='autoplay=1&origin=',
)

register_setting(
    name="PAGES4GOV_YOUTUBE_EMBED_WIDTH",
    description="",
    editable=True,
    default='640',
)

register_setting(
    name="PAGES4GOV_YOUTUBE_EMBED_HEIGHT",
    description="",
    editable=True,
    default='390',
)