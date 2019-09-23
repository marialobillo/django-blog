from django.shortcuts import render
from django.views.generic import ListView, DetailsView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailsView(DetailView):
    model = Post
    template_name = 'post_detail.html'
