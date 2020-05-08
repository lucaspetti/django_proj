# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post

def home(request):
  context = {
    'posts': Post.objects.all(),
    'title': 'All posts'
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')
