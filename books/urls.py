from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailsView.as_view(), name="book_details"),
    path('publishers/', views.PublisherView.as_view(), name="publishers"),
    path('publishers/<int:pk>/', views.PublisherDetailsView.as_view(), name="pub_details")
]