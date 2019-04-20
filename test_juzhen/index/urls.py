# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^add/$', add_views, name='add'),
    url(r'^get_date/$', get_date, name='get_date'),
    url(r'^chat/$', chat_views, name='chat_views')
]
