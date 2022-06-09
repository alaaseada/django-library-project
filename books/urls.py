from django.urls import path
from . import views

name = "books"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('publishers/', views.PublisherView.as_view(), name="publishers")
]