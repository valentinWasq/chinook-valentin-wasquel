from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Artist, Album, Track

class IndexView(generic.ListView):
    template_name = 'disks/Index.html'
    context_object_name = 'all_Album'

    def get_queryset(self):
        return Album.objects.all

class detailView(generic.DetailView):
    template_name = 'disks/detail.html'
    model = Album

def recherche(request, rechercheText):
    listAlbum = Album.objects.filter(title__contains=rechercheText)
    context = {'recherche': rechercheText, 'selected_Album': listAlbum}
    return render(request, 'disks/Recherche.html', context)