from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'


class BlogDetail(DetailView):
    model = Blog
    template_name = 'detail.html'


class BlogCreate(CreateView):
    model = Blog
    template_name = 'blog_creat.html'
    fields = ['title', 'auth', 'body']


class BlogUpdate(UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'body']


class BlogDelete(DeleteView):
    model = Blog
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
