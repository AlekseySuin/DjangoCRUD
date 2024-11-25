from django.shortcuts import render, redirect
from .models import Book, Author, Publisher, Genre, User
from .forms import BookForm, AuthorForm, PublisherForm, GenreForm, UserForm
from elasticsearch_dsl.query import Q
from datetime import date

def index(request):
    return render(request, 'books/book_list.html')

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)

def create_book(request):
    form = BookForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('book-list')
    context = {
        'form': form,
        'title': 'Add New Book'
    }
    return render(request, 'create_update_form.html', context)

def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=pk)
    context = {
        'form': form,
        'title': f'Update Book: {book.title}',
        'update': True
    }
    return render(request, 'create_update_form.html', context)

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('book-list')

def search_books(request):
    q = request.GET.get('q')
    if q:
        books = BookDocument.search().query(
            'multi_match', query=q, fields=['title', 'author.first_name', 'author.last_name'])
    else:
        books = ''
    context = {'books': books, 'query': q}
    return render(request, 'search_results.html', context)

# Аналогичные функции для других моделей (Author, Publisher, Genre, User)