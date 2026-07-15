# id is unique num for book
# name is title of book
# quantity is how many copies available
# methods: borrow, return books
# check quantity
# add book (check id)

# Import libraries
import random

# Book (eveything abt the book and print)
class Book:
    def __init__ (self, book_id, book_name):
        self.book_id = book_id
        self.book_name = book_name

# Everything about the user
class User:
    def __init__ (self, id, name):
        self.id = id
        # for i in range(10):
        #     self.id = random.randint(1000000000,9999999999)
        self.name = name
        self.borrowed = []
    
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

library_inventory = {}
admin = Admin()

book1 = admin.add_book(1936482749, "The Hunger Game")
library_inventory[book1.book_name] = 2

book2 = admin.add_book(3456456576, "The Starvation Games")
library_inventory[book2.book_name] = 2

user1 = admin.add_user(1234567890, "Spongebob Squarepants")

book_to_find = "The Starvation Games"

if book_to_find in library_inventory:

    if book_to_find in user1.borrowed:
        print("Sorry, you borrow two of the same book.")

    elif library_inventory[book_to_find] >= 1:
        library_inventory[book_to_find] -= 1
        user1.borrowed.append(book_to_find)

    else:
        print("Sorry, this book isn't available.")

else:
    print("Book was not found.")

print("Hello.")
print(library_inventory)
print(user1.borrowed)

# Menu
# menu = {
#     1936482749 : "The Hunger Game",
#     3456456576 : "The Starvation Games",
#     1293874659 : "The Object Games",
#     2304871348 : "The Blue Games",
#     2734813874 : "How To Kill A Bird"
# }

# quantity = {
#     "The Hunger Game": 2,
#     "The Starvation Games": 2,
#     "The Object Games": 2,
#     "The Blue Games": 2,
#     "How To Kill A Bird": 2
#     }


# chosen book = inputs "the blue games"
# chosen book = chosen book.title()
# print(Book(chosen book))

# playing = True

# print("Welcome to the Cuzanne Sollins Library!")
# name = input("Please enter your full name: ")
# print("")

# while playing:
#     print("Here are the books we have:")
#     print("")
#     print(menu)
#     print("")
#     print("Quantity of copies available for each book: ")
#     print(quantity)
#     print("")
#     book = input("Which book(s) would you like to checkout (q to quit): ")
#     book = book.title()
    
#     if book == "q" or book == "Q":
#         print("Thank you for visiting the Cuzanne Sollins Library!")
#         break

#     elif book in menu.values():
#         print(f"New book checked out: {book}\n")

#         if quantity[book] >= 1:
#             quantity[book] -= 1
            
#         else: 
#             print("Sorry, there are no more copies of this book available.\n")

#     elif book not in menu.values():

#         print("Book was not found, please try again.\n")
#         book = input("Which book(s) would you like to checkout (q to quit): ")
#         print("")
#         book = book.title()
