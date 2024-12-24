class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        print(f"Attempting to remove book: {book.title} by {book.author}")
        for element in self.books:
            if element.title.lower() == book.title.lower() and element.author.lower() == book.author.lower():
                self.books.remove(element)
       
    def search_books(self, search_string):
        search_string = search_string.lower()
        matched_books = []
        for book in self.books:
            if search_string in book.title.lower() or search_string in book.author.lower():
                matched_books.append(book)
        return matched_books