# This is the Driver prog for the Textbook

from Person import Person
from Texbook import Textbook
import time

# creates a function for the program


def the_book():
    first = input("What is the author's first name? >>>")
    last = input("What is the author's last name? >>>")
    age = input("How old is the author? >>>")
    # author = str(Person(first, last, age))

    print(f"So, your book was written by {first} {last}, who is {age} years old.")
    print("\n Please tell me more info about the book, so I can find it.")

    input("\n")
    title = input("Please enter the title of the book you're looking for. >>>")
    edition = input("What edition is the book? >>>")
    isbn = input("Please enter the 13-digit ISBN number >>>")
    publisher = input("What company published this textbook? >>>")
    year = input("What year was this book published? >>>")
    quantity = int(input("How many books are in stock? >>>"))
    while quantity < 5:  # sets a min at 5, the user can 'order' more
        print(f"Books in stock = {quantity}")
        print("The stock is too low. We need more books!")
        more = int(input("How many more books do we need? >>>"))
        quantity = quantity + more
        print(f"Books in stock = {quantity}")
        if quantity < 6:
            print("The stock is too low. We still need more books!")
            more = int(input("How many more books do we need? >>>"))
            quantity = quantity + more
            print(f"Books in stock = {quantity}")
        elif quantity > 6:
            break
    while quantity >= 15:  # Sets a max at 15 books
        print("I think we ordered too many textbooks. Let's get rid of some.")
        input()
        print("Trashing textbooks, please wait...")
        time.sleep(2)
        quantity = 9
        print('Okay, we have enough space for 9 textbooks!')
        break
    print(f"Cool, we have {quantity} of '{title}' now.")

    price = input("How much does the book cost? >>>$")

    book1 = Textbook(first, last, age, title, edition, isbn, publisher, year, quantity, price)
    #  Here we will get the second book's information

    print("Okay, just help me with one more book and you're free to go.")
    input()
    first2 = str(input("What is the 2nd author's first name? >>>"))
    last2 = str(input("What is their last name? >>>"))
    age2 = str(input("How old are they? >>>"))

    print(f"So, the 2nd book was written by {first2} {last2}, who is {age2} years old.")
    print("\nTell me more info about the book, so I can find it.")

    input("\n")
    title2 = input("Please enter the title of the book you're looking for. >>>")
    edition2 = input("What edition is the book? >>>")
    isbn2 = input("Please enter the 13-digit ISBN number >>>")
    publisher2 = input("What company published this textbook? >>>")
    year2 = input("What year was this book published? >>>")
    quantity2 = int(input("How many books are in stock? >>>"))
    while quantity2 < 5:
        print(f"Books in stock = {quantity2}")
        print("The stock is too low. We need more books!")
        more = int(input("How many more books do we need? >>>"))
        quantity2 = quantity2 + more
        print(f"Books in stock = {quantity2}")
        if quantity2 < 6:
            print("The stock is too low. We still need more books!")
            more = int(input("How many more books do we need? >>>"))
            quantity2 = quantity2 + more
            print(f"Books in stock = {quantity2}")
        elif quantity2 > 6:
            break
    while quantity2 >= 15:
        print("I think we ordered too many textbooks. Let's get rid of some.")
        input()
        print("Trashing textbooks, please wait...")
        time.sleep(2)
        quantity2 = 9
        print('Okay, we have enough space for 9 textbooks!')
        break
    print(f"Cool, we have {quantity2} of '{title2}' now.")
    price2 = input("How much does the book cost? >>>$")
    book2 = Textbook(first2, last2, age2, title2, edition2, isbn2, publisher2, year2, quantity2, price2)

    #  Here we will display the book info
    print("Compiling data, please wait...")
    time.sleep(2)
    print("I found the books you're looking for!")
    input("Press ENTER to view the information.")
    print(f"""  
    {title}, by {first} {last}.
    Edition #{edition}
    ISBN - {isbn}
    Published by {publisher} in {year}.
    We have {quantity} in stock, for a price of ${price} per textbook.""")
    print(f"""\n
    {title2}, by {first2} {last2}.
    Edition #{edition2}
    ISBN - {isbn2}
    Published by {publisher2} in {year2}.
    We have {quantity2} in stock, for a price of ${price2} per textbook.""")

# exe
print("""
Welcome to the Library, LOSER.
Today, you are starting your new job as a librarian.""")
input("\nPress ENTER to continue")
print("\nWe should call you, 'Loser the Librarian'!!")
print("Anyway, this job is simple.")
print("Just give me the information of the book, and I'll help you keep inventory.")
input("\nPress ENTER to continue")
the_book()
