# Markhus Dammar
# 11/20/19
# This creates the textbook class

from Person import Person


class Textbook():

    def __init__(self, first, last, age, title, edition, isbn, publisher, year, quantity, price):
        self.first = first
        self.last = last
        self.age = age
        self.author = str(Person(first, last, age))
        self.title = title
        self.edition = edition
        self. isbn = int(isbn)
        self.publisher = publisher
        self.year = int(year)
        self.quantity = int(quantity)
        self.price = int(price)



