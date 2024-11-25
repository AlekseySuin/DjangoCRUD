from django import forms
from .models import Book, Author, Publisher, Genre, User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'