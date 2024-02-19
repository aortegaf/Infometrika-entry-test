from django.shortcuts import render
from .models import Book, Writer

def home(request):
    all_books = Book.objects.all
    writer_info = Writer.objects.all
    return render(request, 'home.html', {'library':all_books, 'writer': writer_info})

def writers(request):
    all_books = Book.objects.all
    writer_info = Writer.objects.all
    return render(request, 'writers.html', {'library':all_books, 'writers': writer_info})
