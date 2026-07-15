import random


class Book:
   def __init__ (self, book_id, book_name):
       self.book_id = book_id
       self.book_name = book_name


# Everything about the user
class User:
   def __init__ (self, id, name):
       self.id = id
       self.name = name
       self.borrowed = []
   def __str__(self):
        return f"User ID: {self.id} | Name: {self.name}"


   # def borrowed_books (self, borrow_book):
   #     self.borrowed.append(borrow_book)


# EVERYTHING
class Admin:
   def add_book(self, book_id, book_name):
       new_book = Book(book_id, book_name)
       return new_book
 
   def add_user(self, id, name):
       new_user = User(id, name)
       return new_user


# Starting variables
playing = True
book_to_find = ""
user1 = ""
library_inventory = {}
admin = Admin()


book1 = admin.add_book(1936482749, "The Hunger Game")
library_inventory[book1.book_name] = 2


book2 = admin.add_book(3456456576, "The Starvation Games")
library_inventory[book2.book_name] = 2


book3 = admin.add_book(1293874659, "The Object Games")
library_inventory[book3.book_name] = 2


book4 = admin.add_book(2304871348, "The Blue Games")
library_inventory[book4.book_name] = 2


book5 = admin.add_book(2734813874, "How To Kill A Bird")
library_inventory[book5.book_name] = 2




# Input

print("")
print("Welcome to the Cuzanne Sollins Library!")
name = input("Please enter your name: ")
print("")


# User id
for i in range(10):
    id = random.randint(1000000000,9999999999)


user1 = admin.add_user(id, name)


print(user1)
print("")


# Starting the loop
while playing:
    print(library_inventory)
    print("")


    # Looking for the right book
    book_to_find = input("What book(s) are you interested in today?: ")
    print("")


    # Make the book a title
    book_to_find = book_to_find.title()


    # Checking if the book is in system
    if book_to_find in library_inventory:


    # User already has it
        if book_to_find in user1.borrowed:
            print("Sorry, you can't borrow two of the same book.")
            print("")


    # If it is in system
        elif library_inventory[book_to_find] >= 1:
            library_inventory[book_to_find] -= 1
            user1.borrowed.append(book_to_find)
            print("SUCCESS. You have now borrowed:",book_to_find)
            print("")


   # It is not in system
        else:
            print("Sorry, this book isn't available.")


    # If it is random
    else:
        print("Book was not found.")
        print("")
   
    # Ask the user to quit
    quit = input("Quit? (y/n): ")
    print("")
    quit = quit.upper()


    if quit == "Q" or quit =="QUIT" or quit == "YES" or quit == "Y":
        print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")
        print("Thank you for visitng the Cuzanne Sollins Library!")
        print("")
        print("BORROWED BOOKS:", user1.borrowed)
        print("")
        break