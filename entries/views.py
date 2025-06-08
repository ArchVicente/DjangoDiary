from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry
# Create your views here.

class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-created_at') # Order by created_at in descending order

class EntryDetailView(DetailView):
    model = Entry