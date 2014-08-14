from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category

class ListPostsView(ListView):
    """
    View to list all posts.
    """
    model = Post
    template_name = "list_posts.html"
    context_object_name = "posts"

class DetailPostView(DetailView):
    """
    View to detail all posts.
    """
    model = Post
    template_name = "detail_post.html"