'''
Library Management System:
-------------------------
Entities:
•	Book: Contains details about a book (title, author).
•	User: A base class for people who borrow books.
•	Student and Faculty: Types of users with different borrowing limits.
Steps:
1.	Book Class:
    a.	Attributes: title, author.
    b.	Methods: display_info(), which shows book details.
2.	User Class:
    a.	Attributes: name, max_books (determines the borrowing limit).
    b.	Methods:
        i.	borrow_book(book): Adds a book to the borrowed list.
        ii.	return_book(book): Removes a book from the borrowed list.
3.	Inheritance:
        a.	Student inherits from User and has a limit of 3 books.
        b.	Faculty inherits from User and has a limit of 5 books.
4.	Polymorphism:
        a.	Both Student and Faculty override borrow_book() to check if they have exceeded their limits.
Example Problem:
•	Create a Student and a Faculty object, borrow and return books, and display how many books each user has.

'''

# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author = author
#
#
#     def display_info(self):
#         print(f'Book is {self.title}  |  Author name is  {self.author}')
#
# class User:
#     def __init__(self, name, max_books):
#         # super().__init__(self.title,self.author)
#         self.name = name
#         self.max_books = max_books
#         self.borrowed = []
#
#     def borrow_book(self,book):
#         if book not in self.borrowed  or book in self.borrowed:
#             self.borrowed.append(book)
#             print(f'Books is list {self.name} and {book.title}')
#         else:
#             print('Invalid Book name')
#
#     def return_book(self,book):
#         if book in self.borrowed:
#             self.borrowed.remove(book)
#             print(f'Book list {self.borrowed} and return book {book.title}')
#         else:
#             print('Book is Invalid')
#
#
# class Student(User):
#     def __init__(self,name,max_books):
#         super().__init__(name,max_books=3)
#         self.name = name
#
#
#     def student_book(self,book):
#         if len(self.borrowed) <= self.max_books:
#             self.borrowed.append(book)
#             print(f'Student book details {self.borrowed} and title {book.title}')
#         else:
#             print('student borrowed limit is max=3')
#
#
# class Faculty(User):
#     def __init__(self,name,max_books):
#         super().__init__(max_books=5)
#         self.name=name
#
#     def faculty_book(self,book):
#         if len(self.borrowed) <= self.max_books:
#             self.borrowed.append(book)
#             print(f'faculty book details {self.borrowed} and title {book.title}')
#         else:
#             print('faculty borrowed limit is max=5')
#
# b1=Book('python','vansun')
# student = Student("Haresh",3)
# student.student_book(b1)
# faculty = Faculty("Dr. Smith")

#==========================================================================================

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f'Book title is {self.title} and author is  {self.author}')

class User:
    def __init__(self,name,max_books):
        self.name = name
        self.max_book = max_books
        self.borrowed =[]
        # self.count = 0

    def return_book(self,book):
        if book in self.borrowed :
            self.borrowed.remove(book)
            # self.count = self.count - 1
            print(f'Book name is {book.title} and {self.max_book}')
        else:
            print('Book is Invalid')

class Student(User):
    def __init__(self,name):
        super().__init__(name,max_books =3)

    def borrow_book(self,book):
        if len(self.borrowed) < self.max_book :
            self.borrowed.append(book)
            # self.count = self.count + 1
            print(f'book name is {book.title}')
        else:
            print('Books limitation is completed')



class Faculty(User):
    def __init__(self,name):
        super().__init__(name,max_books=5)

    def borrow_book(self,book):
        if len(self.borrowed) < self.max_book :
            self.borrowed.append(book)
            # self.count = self.count + 1
            print (f'book name is {len(self.borrowed)}')
        else:
            print ('Books limitation is completed')



# Create books
b1 = Book("Python", "Guido")
b2 = Book("Java", "James Gosling")

# Create users
student = Student("Haresh")
faculty = Faculty("Dr. Smith")

# Borrow books
student.borrow_book(b1)
student.borrow_book(b2)

faculty.borrow_book(b1)

# Return book
student.return_book(b1)

# Display borrowed count
print("Student borrowed books:", len(student.borrowed))
print("Faculty borrowed books:", len(faculty.borrowed))








# b1=Book('Python','Vangasum')
# b2=Book('Java','krish')
# b3=Book('SQL','HEllo')
# b4=Book('Python','Vangasum')
# b5=Book('Java','Vangasum')
# b6=Book('DE','superi')
# # student = Student('Harish')
# # student.borrow_book(b1)
# # student.borrow_book(b2)
# # student.borrow_book(b3)
# # student.borrow_book(b4)
#
# faculty = Faculty('Ishi')
# faculty.borrow_book(b1)
# faculty.borrow_book(b2)
# faculty.borrow_book(b3)
# faculty.borrow_book(b4)
# faculty.borrow_book(b5)
# faculty.borrow_book(b6)

