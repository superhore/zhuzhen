# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

import re
import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .models import *


def add_views(request):
    s=0
    if request.method == 'POST':
        if request.POST:
            for x in request.POST.values():
                s += int(x)
            print(s)

        return JsonResponse({'a,b和爲':s})


def get_date(request):
    if request.method == 'GET':
      # return HttpResponse(str(datetime.datetime.now()))
       return JsonResponse({'new_time':str(datetime.datetime.now())})


def chat_views(request):
    if request.method == 'POST':
        print('aaaaa')
        msg = request.POST.get('msg')

        if re.search('您好', msg) and re.search('再见',msg):
            print('天氣不錯')
            return JsonResponse({'data':'天气不错'})

        elif re.search('您好', msg):
            print(type(re.search('您好', msg)))
            print('您好，您吃了吗？')
            return JsonResponse({'data':'您好，您吃了吗？'})
        elif re.search('再见'):
            print('回见了您内。')
            return JsonResponse({'data':'回见了您内。'})
        
