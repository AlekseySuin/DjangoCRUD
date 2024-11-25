from django.shortcuts import render, redirect
from .models import Book, Author, Publisher, Genre, User
from .forms import BookForm, AuthorForm, PublisherForm, GenreForm, UserForm
from .documents import BookDocument
from elasticsearch_dsl.query import Q
from datetime import date

def index(request):
    return render(request, 'books/book_list.html')

def book_list(request):
    books = Book.objects.all()[:10]
    context = {'books': books}
    return render(request, 'books/book_list.html', context)

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
    return render(request, 'books/create_book.html', context)

def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('update-book', pk=pk)
    context = {
        'form': form,
        'title': f'Update Book: {book.title}',
        'update': True
    }
    return render(request, 'books/update_book.html', context)

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('book-list')

def create_author(request):
    form = AuthorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('book-list')
    context = {
        'form': form,
        'title': 'Add New Author'
    }
    return render(request, 'books/create_author.html', context)

def update_author(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(instance=author)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=pk)
    context = {
        'form': form,
        'title': f'Update Book: {author.title}',
        'update': True
    }
    return render(request, 'books/update_author.html', context)

def delete_author(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect('book-list')

def create_genre(request):
    form = GenreForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('book-list')
    context = {
        'form': form,
        'title': 'Add New Author'
    }
    return render(request, 'books/create_genre.html', context)

def update_genre(request, pk):
    genre = Genre.objects.get(id=pk)
    form = GenreForm(instance=genre)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=pk)
    context = {
        'form': form,
        'title': f'Update Book: {genre.title}',
        'update': True
    }
    return render(request, 'books/update_genre.html', context)

def delete_genre(request, pk):
    genre = Genre.objects.get(id=pk)
    genre.delete()
    return redirect('book-list')

def create_publisher(request):
    form = PublisherForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('book-list')
    context = {
        'form': form,
        'title': 'Add New Author'
    }
    return render(request, 'books/create_publisher.html', context)

def update_publisher(request, pk):
    publisher = Publisher.objects.get(id=pk)
    form = GenreForm(instance=publisher)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=pk)
    context = {
        'form': form,
        'title': f'Update Book: {publisher.name}',
        'update': True
    }
    return render(request, 'books/update_publisher.html', context)

def delete_publisher(request, pk):
    genre = Genre.objects.get(id=pk)
    genre.delete()
    return redirect('book-list')

def search_books(request):
    q = request.GET.get('q')
    if q:
        books = BookDocument.search().query(
            'multi_match', query=q, fields=['title', 'author.first_name', 'author.last_name'])
    else:
        books = ''
    context = {'books': books, 'query': q}
    return render(request, 'books/book_list.html', context)

# Аналогичные функции для других моделей (Author, Publisher, Genre, User)