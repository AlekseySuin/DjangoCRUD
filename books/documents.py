from django_elasticsearch_dsl import(Document, Index, fields)
from .models import Book, Author, Publisher, Genre, User

book_index = Index('books')
author_index = Index('authors')
publisher_index = Index('publishers')
genre_index = Index('genres')
user_index = Index('users')

@book_index.doc_type
class BookDocument(Document):
    class Django:
        model = Book
        fields = ['title', 'published_date']
        related_models = [Author, Publisher, Genre]

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Author):
            return related_instance.book_set.all()
        elif isinstance(related_instance, Publisher):
            return related_instance.book_set.all()
        elif isinstance(related_instance, Genre):
            return related_instance.book_set.all()

@author_index.doc_type
class AuthorDocument(Document):
    class Django:
        model = Author
        fields = ['first_name', 'last_name']

@publisher_index.doc_type
class PublisherDocument(Document):
    class Django:
        model = Publisher
        fields = ['name']

@genre_index.doc_type
class GenreDocument(Document):
    class Django:
        model = Genre
        fields = ['name']

@user_index.doc_type
class UserDocument(Document):
    class Django:
        model = User
        fields = ['username', 'email']