from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_list.html'
    context_object_name = 'bookmark_list'


class BookmarkDetailView(DetailView):
    model = Bookmark
    template_name = 'bookmark/detail.html'
    context_object_name = 'bookmark_detail'


