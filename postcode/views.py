from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import DisplayLocation

class PostcodeListView(ListView):
    model = DisplayLocation
    template_name = 'home.html'

class PostcodeDetailView(DetailView):
    model = DisplayLocation
    template_name = 'post_detail.html'

class PostcodeCreateView(CreateView):
    model = DisplayLocation
    template_name = 'post_new.html'
    fields = '__all__'

class PostcodeUpdateView(UpdateView):
    model = DisplayLocation
    fields = ['area', 'postcode']
    template_name = 'post_edit.html'

class PostcodeDeleteView(DeleteView):
    model = DisplayLocation
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class SearchResultsView(ListView):
    model = DisplayLocation
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = DisplayLocation.objects.filter(
            Q(area__icontains=query) | Q(postcode__icontains=query)
        )
        return object_list