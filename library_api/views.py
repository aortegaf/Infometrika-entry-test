from django.shortcuts import render
from .models import Book, Author

def home(request):
    all_books = Book.objects.all
    author_info = Author.objects.all
    return render(request, 'home.html', {'library':all_books, 'author': author_info})

def update(request):
    book = Book.objects.all
    author = Author.objects.all
    return render(request, 'update.html', {'book_info':book, 'author_info': author})
       

def test(request):
    all_books = Book.objects.all
    return render(request, 'test.html', {'library':all_books})

