# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'blog/home.html')

def about(request):
  return HttpResponse('blog/about.html')
