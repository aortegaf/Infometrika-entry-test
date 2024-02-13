from django.shortcuts import render
from .models import Book, Author

def home(request):
    all_books = Book.objects.all
    author_info = Author.objects.all
    return render(request, 'home.html', {'library':all_books, 'author': author_info})

