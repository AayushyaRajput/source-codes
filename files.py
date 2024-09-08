#Central Library Management

class library:
    def __init__(self, file_path):
    
        self.books = []
        try:
            with open(file_path, 'r') as file:
                self.books = [line.strip().lower() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")

    def availablebooks(self):
        print("The books which is available: ")
        for books in self.books:
            print("*",books.title())

    def borrowbooks(self,bookname):
        bookname = bookname.lower()
        if bookname in self.books:
            print(f"Thank you! Your {bookname} book has been issued. \nPlease return within 30 days.  ")
            self.books.remove(bookname) 
            return True
        else:
            print("Currently this book is not Available in Library check with Librarian please.")
            return False
         
    def returnbook(self,bookname):
        bookname = bookname.lower()
        self.books.append(bookname)
        if bookname in self.books:
            print("Thanks for returning this book. We hope you enjoyed it.")

class student:
    def requestbooks(self):
        self.book = input("Write the name of the book: ")
        return self.book
    
    def returnbooks(self):
        self.book = input("Write the book name: ")
        return self.book

if __name__=="__main__":    
    file_path = "files.txt"
    centrallib = library(file_path)
    Student = student()

    try:
        while(True):
            msg = '''****Central Library Delhi****
                    1 List of the books
                    2 Borrow book
                    3 Return and donate a book
                    4 Exit'''
            print(msg)
            a = int(input("Hello! Welcome to the Delhi Public Library. please choose an option: "))
        
            if a==1:
                centrallib.availablebooks()
            elif a==2:
                centrallib.borrowbooks(Student.requestbooks()) 
            elif a==3:
                centrallib.returnbook(Student.returnbooks()) 
            else:
                print("Thank you for visiting, Please share your views")    
                exit()

    except ValueError:
        print("Invalid selection. Please choose a valid option.")
