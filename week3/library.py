class Library:
    def __init__(self):
        self.books = []  
    
    def add_book(self, book_title):
        self.books.append(book_title)  
    
    def show_books(self):
        if not self.books:  
            print("The library has no books.")
        else:
            print("Books in the library:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")


library = Library()

library.add_book("Python Crash Course")
library.add_book("Clean Code")
library.add_book("The Pragmatic Programmer")


library.show_books()


empty_lib = Library()
empty_lib.show_books()