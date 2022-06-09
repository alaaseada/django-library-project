from ast import List
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Book, Author, Publisher

import books

# Create your views here.
class IndexView(ListView):
    model = Book
    template_name = "books/index.html"



class PublisherView(ListView):
    model = Publisher
