# Base class
class Book:
    def __init__(self, title, author, isbn, pages, price):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__pages = pages
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_pages(self):
        return self.__pages

    def get_price(self):
        return self.__price


# Derived class 1
class ReferenceBook(Book):
    def __init__(self, title, author, isbn, pages, price, reference_type):
        super().__init__(title, author, isbn, pages, price)
        self.__reference_type = reference_type

    def get_reference_type(self):
        return self.__reference_type

    def display_details(self):
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")
        print(f"ISBN: {self.get_isbn()}")
        print(f"Pages: {self.get_pages()}")
        print(f"Price: {self.get_price()}")
        print(f"Reference Type: {self.get_reference_type()}")


# Derived class 2
class FictionBook(Book):
    def __init__(self, title, author, isbn, pages, price, genre):
        super().__init__(title, author, isbn, pages, price)
        self.__genre = genre

    def get_genre(self):
        return self.__genre

    def display_details(self):
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")
        print(f"ISBN: {self.get_isbn()}")
        print(f"Pages: {self.get_pages()}")
        print(f"Price: {self.get_price()}")
        print(f"Genre: {self.get_genre()}")


# Library class
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.get_title()] = book

    def display_all_books(self):
        for book in self.books.values():
            book.display_details()
            print("------------------------")

    def search_book(self, title):
        if title in self.books:
            self.books[title].display_details()
        else:
            print(f"Book '{title}' not found.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' removed.")
        else:
            print(f"Book '{title}' not found.")


# Main function
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Choose an option or type a command: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            pages = int(input("Enter book pages: "))
            price = float(input("Enter book price: "))
            book_type = input("Enter book type (Reference/Fiction): ")

            if book_type.lower() == "reference":
                reference_type = input("Enter reference type: ")
                book = ReferenceBook(title, author, isbn, pages, price, reference_type)
            elif book_type.lower() == "fiction":
                genre = input("Enter book genre: ")
                book = FictionBook(title, author, isbn, pages, price, genre)
            else:
                print("Invalid book type.")
                continue

            library.add_book(book)
        elif choice == "2":
            library.display_all_books()
        elif choice == "3":
            title = input("Enter book title to search: ")
            library.search_book(title)
        elif choice == "4":
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == "5":
            print("Goodbye! Thank you for using the Library Management System.")
            break
        elif choice.startswith("add "):
            title = choice[4:]
            # ... (add book code using title)
        elif choice.startswith("search "):
            title = choice[7:]
            library.search_book(title)
        elif choice.startswith("remove "):
            title = choice[7:]
            library.remove_book(title)
        else:
            print("Invalid option. Please choose a valid option or type a command.")


if __name__ == "__main__":
    main()
    print("Library Management System terminated.")

