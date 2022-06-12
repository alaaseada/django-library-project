# from django.shortcuts import render
# from django.http import HttpResponse
from urllib import request
from django.views.generic import ListView, DetailView
from .models import Book, Author, Publisher
from datetime import datetime

import books

# Create your views here.
class IndexView(ListView):
    model = Book
    context_object_name = "books_list"
    template_name = "books/index.html"

    def get_queryset(self):
        return Book.objects.filter(publication_date__lte=datetime.today().date()).order_by('-publication_date')[:5]



class DetailsView(DetailView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(pk=self.kwargs['pk'], publication_date__lte=datetime.today().date())


class PublisherView(ListView):
    model = Publisher


class PublisherDetailsView(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['publisher'] = self.object
        context['books_list'] = Book.objects.filter(publisher_id=self.object.id)
        return context
