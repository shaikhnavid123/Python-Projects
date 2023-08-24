"""
Create a library class :
display book
lend book - (who owns the book if not present)
add book
return book

ElliotLibrary = Library(listofbooks, library name)
dictionary (books-nameofperson)

create a main function and run an infinite while loop asking users for their input
"""

class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library : {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been addded to book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    elliot = Library(['Python Handbook','Python-Flask framework','Guide for C++','Java for Beginners'],"ElliotAlderson")

    while(True):
        print(f"Welcome to the {elliot.name} library.\n Enter your choice to continue")
        print("1. Display Book")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")

        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            elliot.displayBooks()
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:\n")
            name = input("Enter your name :\n")
            elliot.lendBook(name, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:\n")
            elliot.returnBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:\n")

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2=""
        while user_choice2!="c" and user_choice2!="q":
            user_choice2 = input()
            if user_choice2=="q":
                exit()
            if user_choice2=="c":
                continue