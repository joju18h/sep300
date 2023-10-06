class User:
    def __init__(self, name, uid, books):
        self.name = name
        self.id = uid
        self.books = books

    def borrow_book(self, book):
        self.books.append(book)

    def return_book(self, book):
        self.books.remove(book)

    def display_info(self):
        print("Name: ",self.name)
        print("ID: ",self.id)
        print("User's books: ")
        for book in self.books:
            print(book)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("ISBN: ",self.isbn)


