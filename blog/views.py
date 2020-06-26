from django.views.generic import ListView, DetailView, edit
from django.urls import reverse_lazy
from .models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class BlogCreateView(edit.CreateView):
    model = Post
    template_name = 'blog/create.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(edit.UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'body']


class BlogDeleteView(edit.DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:home')
