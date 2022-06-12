from urllib import response
from django.test import TestCase
from datetime import datetime, timedelta
from .models import Book, Publisher
from django.urls import reverse

def create_a_book(publication_date, title='title', cover='none.jpg'):
        publisher = Publisher.objects.create(name='name', address='address', country='country', city='city', state='state', website='website.com')
        book = Book.objects.create(title=title, publication_date=publication_date, publisher_id=publisher.id,cover=cover)
        return book


# Create your tests here.
class BookIndexViewTests(TestCase):

    def test_is_published_recently(self):
        book = create_a_book((datetime.now() + timedelta(days=30)).date())
        self.assertIs(book.is_published_recently(), False)


    def test_view_no_books(self):
        response = self.client.get(reverse('books:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No books are available')
        self.assertQuerysetEqual(response.context['books_list'], [])


    def test_view_published_books(self):
        response = self.client.get(reverse('books:index'))
        book = create_a_book((datetime.now() - timedelta(days=30)).date())
        self.assertQuerysetEqual(response.context['books_list'], [book])

    
    def test_view_unpublished_books(self):
        book = create_a_book((datetime.now() + timedelta(days=30)).date())
        response = self.client.get(reverse('books:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No books are available')
        self.assertQuerysetEqual(response.context['books_list'], [])

    
    def test_view_with_published_and_unpublished_books(self):
        to_be_published_book = create_a_book((datetime.now() + timedelta(days=30)).date())
        already_published_book = create_a_book((datetime.now() - timedelta(days=30)).date())
        response = self.client.get(reverse('books:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['books_list'], [already_published_book])

    
    def test_multiple_published_books(self):
        published_book1 = create_a_book((datetime.now() - timedelta(days=30)).date())
        published_book2 = create_a_book((datetime.now() - timedelta(days=1)).date())
        response = self.client.get(reverse('books:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['books_list'], [published_book1, published_book2])



class BookDetailViewTests(TestCase):

    def test_published_books_details(self):
        published_book = create_a_book(title="published_book", publication_date=(datetime.now() - timedelta(days=30)).date())
        response = self.client.get(reverse('books:book_details', args=(published_book.id,)))
        self.assertContains(response, published_book.title)


    def test_unpublished_books_details(self):
        unpublished_book = create_a_book(title="unpublished_book", publication_date=(datetime.now() + timedelta(days=30)).date())
        response = self.client.get(reverse('books:book_details', args=(unpublished_book.id,)))
        self.assertEqual(response.status_code, 404)