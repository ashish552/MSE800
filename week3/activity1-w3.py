class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
         return (f"{self.title} by {self.author} ({self.year})")
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        print(f"Book '{title}' added to a library")

    def show_books(self):
        if not self.books:
            print("The library is empty")
        else:
            print("Books im the library:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")

def main():
    library = Library()

    while True:
        print("\n===== library book manager =======")
        print("1. Add book")
        print("2. show books")
        print ("3. Exit")

        choice = input("Enter choice from 1 - 3 ")

        if choice == "1":
            title = input ("enter title of the book:")
            author = input("Enter author name of the book:")
            year = input("enter publication year: ")
            library.add_book(title, author, year)
        elif choice == "2":
            library.show_books()
        elif choice == "3":
            print("Exiting library book Manager")
            break
        else:
            print("Invalid choice. Please enter number between 1 and 3 . Thank you")

if __name__ == "__main__":
    main()
