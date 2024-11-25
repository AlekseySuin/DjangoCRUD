import random
from faker import Faker
from .models import Author, Publisher, Genre, Book, User

fake = Faker()


def generate_authors(n):
    authors = []
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        try:
            author = Author.objects.create(first_name=first_name, last_name=last_name)
            authors.append(author)
            print(f"Created author: {author}")
        except Exception as e:
            print(f"Failed to create author: {e}")
    return authors


def generate_publishers(n):
    publishers = []
    for _ in range(n):
        name = fake.company()
        try:
            publisher = Publisher.objects.create(name=name)
            publishers.append(publisher)
            print(f"Created publisher: {publisher}")
        except Exception as e:
            print(f"Failed to create publisher: {e}")
    return publishers


def generate_genres(n):
    genres = []
    for _ in range(n):
        name = fake.word()
        try:
            genre = Genre.objects.create(name=name)
            genres.append(genre)
            print(f"Created genre: {genre}")
        except Exception as e:
            print(f"Failed to create genre: {e}")
    return genres


def generate_users(n):
    users = []
    for _ in range(n):
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=10)
        try:
            user = User.objects.create(username=username, email=email, password=password)
            users.append(user)
            print(f"Created user: {user}")
        except Exception as e:
            print(f"Failed to create user: {e}")
    return users


def generate_books(n, authors, publishers, genres):
    books = []
    for _ in range(n):
        title = fake.sentence(nb_words=6)[:-1].title()
        published_date = fake.date_between(start_date='-50y', end_date='today')
        author = random.choice(authors)
        publisher = random.choice(publishers)
        gende = random.choice(genres)
        try:
            book = Book.objects.create(title=title, author=author, publishers=publisher, gende=gende, published_date=published_date)
            books.append(book)
            print(f"Created book: {book}")

            # Присваивание жанров книгам
            book.genre.set(random.sample(genres, k=random.randint(1, len(genres))))
        except Exception as e:
            print(f"Failed to create book: {e}")


n = 100
authors = generate_authors(n)
publishers = generate_publishers(n)
genres = generate_genres(n)
users = generate_users(n)
generate_books(n * 2, authors, publishers, genres)