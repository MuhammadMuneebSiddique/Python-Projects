
# Person Class
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

# Member Class
class Member(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.book = []

    # Borrow Book Function
    def borrow_book(self,book_id,library):
        for items in library.books:
            if items["id"] == book_id:
                self.book.append(items["title"])
                items["isavailable"] = False
    
    # Return Book Function
    def return_book(self,book_id,library):
        for items in library.books:
            if items["id"] == book_id:
                items["isavailable"] = True

    # Get Member Details
    def get_details(self):
        print("\n ------ Member Details ------ \n")
        print("Member Name :",self.name)
        print("Member Age :",self.age)
        print("Book Borrow :",self.book)

# Librarian Class
# Add_Book and Remove_Book Function 
class Librarian(Person):
    def __init__(self, name, age , salary):
        super().__init__(name, age)
        self.salary = salary
    
    # Add Book in Library
    def add_book(self,book,library):
        library.books.append({"id":book.id,"title":book.title,"author":book.author,"isavailable":True})
    
    # Remove Book In Library
    def remove_book(self,id,library):
        for book in library.books:
            if book["id"] == id:
                library.books.remove(book)
                print("Book Remove Succesfully in Library")

# Creating a new Book Class
class Book():
    def __init__(self,id,book_title,author_name):
        self.id = id
        self.title = book_title
        self.author = author_name
        self.isavailable = False
    
    # Get Book Details Function
    def get_details(self):
        print("\n ------ Book Details ------ \n")
        print("Book Title :",self.title)
        print("Book Author Name :",self.title)
        print("Book Is Available in Library :",self.isavailable)
        print("Book Title :",self.title)

# Creating Library
class Library():
    def __init__(self,name):
        self.name = name
        self.books = []

    def get_details(self):
        print(f"\n ------ {self.name} Library Details ------ \n")
        for items in self.books:
            print(f"Book No {items["id"]} :",items)
        if self.books == []:
            print("EMPTY")


# Test the Library Management System
library = Library("Magic")
librarian = Librarian("Rashid Minhash",23,10000)

b1 = Book(1,"THE MAIN CHARACTER","Muneeb Siddiqui")
b2 = Book(2,"THE LAST NIGHT","Muneeb Siddiqui")
b3 = Book(3,"THE EVIL EYES","Muneeb Siddiqui")

librarian.add_book(b1,library)
librarian.add_book(b2,library)
librarian.add_book(b3,library)
library.get_details()

m1 = Member("Asna",23)
m1.borrow_book(2,library)
m1.get_details()
library.get_details()


