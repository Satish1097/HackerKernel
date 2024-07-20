from django.db import models
import datetime


class Author(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=254)
    bio=models.CharField(max_length=10000)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=256)
    genre=models.CharField(max_length=256)
    published_date=models.DateField(default=datetime.date.today)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Borrow_Record(models.Model):
    user_name=models.CharField(max_length=256)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    borrow_date=models.DateField(default=datetime.date.today)
    return_date=models.DateField(default='')

    def __str__(self):
        return self.user_name
