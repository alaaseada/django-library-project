from asyncio.base_subprocess import WriteSubprocessPipeProto
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ['-name']

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    title = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='authors_pps')

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    cover = models.ImageField(upload_to='books_covers')

    def __str__(self) -> str:
        return self.name