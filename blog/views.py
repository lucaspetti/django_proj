# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

posts = [
  {
    'author': 'Who',
    'title': '1st Blog Post',
    'content': '1st Post',
    'date_posted': 'First May'
  },
  {
    'author': 'Whom',
    'title': '2nd Blog Post',
    'content': '2nd Post',
    'date_posted': 'Second May'
  }
]

def home(request):
  context = {
    'posts': posts,
    'title': 'All posts'
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')
