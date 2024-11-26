from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.book_list, name='book-list'),
    path('books/create/', views.create_book, name='create-book'),
    path('books/<int:pk>/update/', views.update_book, name='update-book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete-book'),

    path('authors/create/', views.create_author, name='create-author'),
    path('authors/<int:pk>/update/', views.update_author, name='update-author'),
    path('authors/<int:pk>/delete/', views.delete_author, name='delete-author'),

    path('genre/create/', views.create_genre, name='create-genre'),
    path('genre/<int:pk>/update/', views.update_genre, name='update-genre'),
    path('genre/<int:pk>/delete/', views.delete_genre, name='delete-genre'),

    path('publisher/create/', views.create_publisher, name='create-publisher'),
    path('publisher/<int:pk>/update/', views.update_publisher, name='update-publisher'),
    path('publisher/<int:pk>/delete/', views.delete_publisher, name='delete-publisher'),

    path('zapros/oldestbook/', views.the_oldest_book, name='oldest-book'),
    path('zapros/newsbook/', views.the_news_book, name='news-book'),

    path('search/', views.search_books, name='search-books'),
    # Аналогичные маршруты для других моделей (Author, Publisher, Genre, User)
]