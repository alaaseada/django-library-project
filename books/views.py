from ast import List
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Book, Author, Publisher

import books

# Create your views here.
class IndexView(ListView):
    model = Book
    context_object_name = "books_list"
    template_name = "books/index.html"



class PublisherView(ListView):
    model = Publisher


class PublisherDetailsView(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['publisher'] = self.object
        context['books_list'] = Book.objects.filter(publisher_id=self.object.id)
        return context
