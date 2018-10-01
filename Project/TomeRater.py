class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email

    def __repr__(self):
        return "User " + str(self.name) + ", email: " + str(self.email) + ", books read : " + len(self.books)

    def __eq__(self, other_user):
        # compares user_books
        return

    def read_book(self, book, rating):
        title = Book.get_title(self)
        print(type(title))
        print(rating)
        User.books[title] = rating
        return

    def get_average_rating(self):
        total = 0
        for values in self.books:
            self.books[value] += total
        average = total / len(self.books)
        return average

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This book's isbn has been updated."

    def add_rating(self, rating):
        if rating <= 4 and rating >= 0:
            return self.ratings.append(rating)
        else:
            return "Invalid Rating"

    def get_average_rating(self):
        total = 0
        for values in self.ratings:
            self.ratings[value] += total
        average = total / len(self.ratings)
        return average

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):
        #compares books
        return

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return str(self.title) + " by " + srt(self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return str(self.title) + ", a " + str(self.level) + " manual on " + str(self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        self = Book(title, isbn)
        return self

    def create_novel(self, title, author, isbn):
        self = Fiction(title, author, isbn)
        return self

    def create_non_fiction(self, title, subject, level, isbn):
        self = Non_Fiction(title, subject,level, isbn)
        return self

    def add_user(self, name, email, user_books=None):
        self = User(email, user_books)
        if user_books == None:
            return
        else:
            for book in user_books:
                self.add_book_to_user(self, book, email, rating=None)

    def add_book_to_user(self, book, email, rating):
        self.create_book
        self.books = User.read_book(book, rating)
        print(self.books)
        Book.add_rating(book, rating)
        self.books[book] += 1

    def print_catalog(self, books):
        for book in self.books:
            print(book)

    def print_users(self, users):
        for user in self.users:
            print(user)

    def most_read_book(self, books):
        highest = self.books[1]
        for book in self.books:
            if self.book[book] > highest:
                highest = self.book[book]
        return highest

    def most_positive_user(self, users):
        highest = self.users[1].get_average_raing()
        for user in self.users:
            if user.get_average_rating() > highest:
                highest = user.get_average_rating()
        return highest
