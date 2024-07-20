from django import forms
import datetime
from .models import Author,Book



class add_author(forms.Form):
    name=forms.CharField(label="Auther Name",max_length=256)
    email=forms.EmailField(label="Enter Email" ,max_length=256)
    bio=forms.CharField(label='Bio',max_length=10000, widget=forms.Textarea)



class add_book(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__( *args,**kwargs)
        self.fields['author'].choices = [(author.id, author.name) for author in Author.objects.all()]

    title=forms.CharField(label="title", max_length=256)
    genre=forms.CharField(label="genre",max_length=256)
    published_date=forms.DateField(label='published_date',widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    author=forms.ChoiceField(label='author',choices=[])


book=Book.objects.all()
class borrow_record(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__( *args,**kwargs)
        self.fields['book'].choices = [(book.id, book.title) for book in Book.objects.all()]

    user_name=forms.CharField(max_length=256)
    book=forms.ChoiceField(label="book",choices=[])
    borrow_date=forms.DateField(label='borrow_date', widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    return_date=forms.DateField(label="return_date", widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
