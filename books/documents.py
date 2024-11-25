from django_elasticsearch_dsl import DocType, Index, fields
from .models import Book, Author, Publisher, Genre, User

book_index = Index('books')
author_index = Index('authors')
publisher_index = Index('publishers')
genre_index = Index('genres')
user_index = Index('users')

@book_index.doc_type
class BookDocument(DocType):
    class Meta:
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
class AuthorDocument(DocType):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

@publisher_index.doc_type
class PublisherDocument(DocType):
    class Meta:
        model = Publisher
        fields = ['name']

@genre_index.doc_type
class GenreDocument(DocType):
    class Meta:
        model = Genre
        fields = ['name']

@user_index.doc_type
class UserDocument(DocType):
    class Meta:
        model = User
        fields = ['username', 'email']