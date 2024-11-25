from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.book_list, name='book-list'),
    path('books/create/', views.create_book, name='create-book'),
    path('books/<int:pk>/update/', views.update_book, name='update-book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete-book'),
    path('search/', views.search_books, name='search-books'),
    # Аналогичные маршруты для других моделей (Author, Publisher, Genre, User)
]