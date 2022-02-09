from django.shortcuts import render
from .models import Book
from .filters import OrderFilter

def home(request):
    all_books = Book.objects.all
    return render(request, 'home.html', {'library':all_books})

def test(request):
    all_books = Book.objects.all
    return render(request, 'test.html', {'library':all_books})

