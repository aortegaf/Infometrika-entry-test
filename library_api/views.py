from django.shortcuts import render
from .models import Book, Writer

def home(request):
    all_books = Book.objects.all
    return render(request, 'home.html', {'library': all_books})

def writers(request):
    all_writers = Writer.objects.all
    return render(request, 'writers.html', {'writers': all_writers})
