from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Post

class PostcodeListView(ListView):
    model = Post
    template_name = 'home.html'
    
class PostcodeDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostcodeCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = '__all__'

class PostcodeUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['area', 'postcode']

class PostcodeDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')