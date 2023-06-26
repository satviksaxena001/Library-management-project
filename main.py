class Library:
    def __init__(self, ListofBooks):
        self.books= ListofBooks
        
    def displayAvailableBooks(self):
        print("Book present in the library: ")
        for book in self.books:
            print("*"+book)

    def borrowBook(self,BookName):
        if BookName in self.books:
            print(f"You have been issued {BookName}. Thank you for issuing")
            self.books.remove(BookName)
            return True

        else:
            print("This bbok is either not avaible or has issued to someone else")
            return False

    def ReturnBook(self,BookName):
        self.books.append(BookName)
        print("Thanks for returning the book.")

class Student:
    def requestBook(self):
        self.books= input("Enterr the book you want to borrow:")
        return self.books
    
    def ReturnBook(self):
        self.books= input("Enter the Book you want to return: ")
        return self.books

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Zero to One"])
    # centralLibrary.displayAvailableBooks()
    student= Student()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a=int(input("Enter the choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")






    