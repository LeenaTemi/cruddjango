from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import ListView
from django.views.generic.edit import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


from .models import BlogApp, Post

# Create your views here.

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
        model = Post
        fields = "__all__"
        success_url: reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post 

class PostUpdateView(UpdateView):
        model = Post
        field = "__all__"
        success_url = reverse_lazy("blog:all")
        
class PostUpdateView(UpdateView):
        model = Post
        field = "__all__"
        success_url = reverse_lazy("blog:all")

        template_name: 'home.html'