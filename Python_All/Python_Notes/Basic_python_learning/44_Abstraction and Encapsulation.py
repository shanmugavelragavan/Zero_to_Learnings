# Abstraction and Encapsulation in Python

# 1. Data abstraction and encapsulation are synonymous as data abstraction is achieved through encapsulation. Abstraction is used to hide internal details and show only functionalities. Abstracting something means to give names to things, so that the name captures the basic idea of what a function or a whole program does. Encapsulation is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.

# 2. This program defines a Python class "Library" with the following attributes and methods:

# . __init__ method: This method is called when an object of the class is created. It initializes the books attribute with the passed books list.
# . list_books method: This method prints the available books list.
# . borrow_book method: This method takes a book name as an argument and removes it from the books list if it is present, or prints a message "Book not Available" otherwise.
# . receive_book method: This method takes a book name as an argument and adds it back to the books list.

# 3 The program then creates an object o of the "Library" class, passing the list of books as an argument. A menu-driven interface is then created using a while loop, which provides the user with three options:

# . Display the list of books
# . Borrow a book
# . Return a book

# 4.The user is prompted to enter their choice, and the corresponding method of the o object is called based on the entered choice. If an invalid choice is entered, the program prints a message "Thank You come again" and quits.

# Abstraction and Encapsulation in Python

class Library:
    def __init__(self,books):
        self.books = books

    def list_books(self):
        print("Available Books")
        for book in self.books:
            print(book)

    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("Get Your Book Now")
            self.books.remove(borrow_book)
        else:
            print("Book Not Available")

    def receive_book(self,receive_book):
        print("You have retturned the book")
        self.books.append(receive_book)

books = ['C', 'C++', 'Java', 'Python', 'Javascript']
o = Library(books)

msg = """
    1.Display Book
    2.Borrow Book
    3.Return Book
"""

while True:
    print(msg)
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        o.list_books()
    elif ch == 2:
        book = input("Enter Book Name To Borrow : ")
        o.borrow_book(book)
    elif ch == 3:
        book = input("Enter Book Name To Return : ")
        o.receive_book(book)
    else:
        print("Thank You Come Again")
        quit()