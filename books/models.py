from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Издатель")

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name="Жанр")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    publishers = models.ForeignKey(Publisher,on_delete=models.CASCADE, verbose_name="Издатель")
    gende = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    published_date = models.DateField(null=False, blank=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=150, unique=True, verbose_name="Имя пользователя")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    password = models.CharField(max_length=128, verbose_name="Пароль")

    def __str__(self):
        return self.username