from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import add_author,add_book,borrow_record
from .models import Author,Book,Borrow_Record
from django.contrib import messages
from django.core.paginator import Paginator
import pandas as pd


def home(req):
    return render(req,'index.html')

def AddAuthor(req):
    if req.method=="POST":
        form=add_author(req.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            email=form.cleaned_data.get('email')
            bio=form.cleaned_data.get('bio')

            Author.objects.create(
                name=name,
                email=email,
                bio=bio
            )
            messages.success(req,"Author Added Successfully")
            return redirect('/')
        else:
            messages.error(req,'All Fields are Required!')
    else:
        form=add_author()
    return render(req,"AddAuthor.html",{"form":form})


def AddBook(req):
    if req.method=='POST':
        form=add_book(req.POST)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            genre=form.cleaned_data.get('genre')
            published_date=form.cleaned_data.get('published_date')
            author_id=form.cleaned_data['author']
            print (author_id)
            if author_id:
                try:
                    author=Author.objects.get(id=author_id)

                    Book.objects.create(
                    title=title,
                    genre=genre,
                    published_date=published_date,
                    author=author
                    )
                except Author.DoesNotExist:
                    messages.error(req,"Author not Exist")
            messages.success(req,'Book Added Successfully!')
            return redirect('/')
        else:
            messages.error(req,'All Fields are Required!')
    else:
        form=add_book()
        return render(req,'AddBook.html',{'form':form})
    
def AddBorrowRecord(req):
    if req.method=='POST':
        form=borrow_record(req.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get('user_name')
            book_id=form.cleaned_data.get('book')
            borrow_date=form.cleaned_data.get('borrow_date')
            return_date=form.cleaned_data.get('return_date')
            if book_id:
                try:
                    book=Book.objects.get(id=book_id)
                    Borrow_Record.objects.create(
                    user_name=user_name,
                    book=book,
                    borrow_date=borrow_date,
                    return_date=return_date
                    )
                except Book.DoesNotExist:
                    messages.error(req,"Book not Available")
            messages.success(req,'Borrow Record Added Successfully!')
            return redirect('/')
        else:
            messages.error(req,'All Fields are Required!')
    else:  
        form=borrow_record()  
        return render(req, 'AddBorrowRecord.html', {"form":form})    


def AuthorRecord(req):
    all_author=Author.objects.all()
    paginator=Paginator(all_author,5)
    page_number=req.GET.get('page')
    authors=paginator.get_page(page_number)
    all_pages=authors.paginator.num_pages
    page_range=[n+1 for n in range(all_pages)]
    return render(req,'AuthorRecord.html',{'authors':authors,'page_range':page_range})

def BookRecord(req):
    all_books=Book.objects.all()
    paginator=Paginator(all_books,5)
    page_number=req.GET.get('page')
    books=paginator.get_page(page_number)
    all_pages=books.paginator.num_pages
    page_range=[n+1 for n in range(all_pages)]
    return render(req,'BookRecord.html',{'books':books,"page_range":page_range})

def BorrowRecord(req):
    all_borrow_records=Borrow_Record.objects.all()
    paginator=Paginator(all_borrow_records,5)
    page_number=req.GET.get('page')
    borrow_records=paginator.get_page(page_number)
    all_pages=borrow_records.paginator.num_pages
    page_range=[n+1 for n in range(all_pages)]
    return render(req,'BorrowRecord.html',{'borrow_records':borrow_records,'page_range':page_range})


def Export_BookRecords(req):
    books=Book.objects.all()

    data=[]
    for book in books:
        data.append({
            'Id':book.id,
            'Title':book.title,
            'Genre':book.genre,
            'Author':book.author.name
        })
    df = pd.DataFrame(data)
    response=HttpResponse(content_type='application/vnd.openxmlformats-officedocuments.spreadsheet.sheet')
    response['Content-Dispossition']='attachment;filename="Books_Records.xlxs"'
    with pd.ExcelWriter(response,engine='openpyxl') as writer:
        df.to_excel(writer,sheet_name='Book_Records,index=false')
    return response
        
def Export_AuthorRecords(req):
    authors=Author.objects.all()

    data=[]
    for author in authors:
        data.append({
            'Id':author.id,
            'Name':author.name,
            'Email':author.email,
            'Bio':author.bio
        })
    df = pd.DataFrame(data)
    response=HttpResponse(content_type='application/vnd.openxmlformats-officedocuments.spreadsheet.sheet')
    response['Content-Dispossition']='attachment;filename="AuthorRecords.xlxs"'
    with pd.ExcelWriter(response,engine='openpyxl') as writer:
        df.to_excel(writer,sheet_name='AuthorRecords,index=false')
    return response


def Export_BorrowRecords(req):
    borrow_rec=Borrow_Record.objects.all()

    data=[]
    for borrow in borrow_rec:
        data.append({
            'Id':borrow.id,
            'UserName':borrow.user_name,
            'Book':borrow.book.title,
            'Borrow Date':borrow.borrow_date,
            'Return Date':borrow.return_date
        })
    df = pd.DataFrame(data)
    response=HttpResponse(content_type='application/vnd.openxmlformats-officedocuments.spreadsheet.sheet')
    response['Content-Dispossition']='attachment;filename="BorrowRecords.xlxs"'
    with pd.ExcelWriter(response,engine='openpyxl') as writer:
        df.to_excel(writer,sheet_name='BorrowRecords,index=false')
    return response