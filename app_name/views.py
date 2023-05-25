from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from .models import post
class HomePageView(ListView):
  model=post
  template_name = 'home.html'
  context_object_name = 'all_posts_list'
class AboutusPageView(TemplateView):
  template_name = 'aboutus.html'