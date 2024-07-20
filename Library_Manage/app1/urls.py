from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('AddAuthor/',views.AddAuthor,name='AddAuthor'),
    path('AddBook',views.AddBook,name='AddBook'),
    path('AddBorrowRecord',views.AddBorrowRecord,name="AddBorrowRecord"),
    path('AutherRecord',views.AuthorRecord,name='AuthorRecord'),
    path('BookRecord',views.BookRecord,name='BookRecord'),
    path('BorrowRecord',views.BorrowRecord,name='BorrowRecord'),
    path('Export_BookRecords',views.Export_BookRecords,name='Export_BookRecords'),
    path('Export_AuthorRecords',views.Export_AuthorRecords,name='Export_AuthorRecords'),
    path('Export_BorrowRecords',views.Export_BorrowRecords,name='Export_BorrowRecords'),



]
