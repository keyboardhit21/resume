from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

class BlogView(ListView):
    model = Blog
    template_name = 'blog_topic.html'
    context_object_name = 'blog'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_view.html'