from django.db import models # type: ignore

from datetime import date

class Author(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date  = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def get_book(self):
        return Book.objects.filter(authors=self)

class Publisher(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name
    def formatted_address(self):
        return f"{self.address} {self.city} {self.state_province} {self.country}"
    
class Book(models.Model):

    title = models.CharField(max_length=200)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)    
    publisher = models.ManyToManyField(Publisher)
    publication_date = models.DateField(default=date.today)
    isbn = models.CharField(max_length=13, unique=True)
                   

    def __str__(self):
        return self.title    
    def book_age(self):

        return date.today().year - self.publication_date.year
    
