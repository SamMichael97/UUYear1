#Practice Task 7
#Write a Python class to represent a book. The Book class should have attributes that reflect the common
#properties of a book– title, author, publisher, page count and price, and provide a constructor method
#alongside appropriate getter and setter functions.
#Test your class with the following Python code that creates a Book object and displays certain details of the
#book:
#book_one = Book("1984", "George Orwell", "Penguin", 336, 6.99 )
#print(book_one.get_title())
#print(book_one.get_author())
#Sample Output
#1984
#George Orwell
#For the upcoming class test, you may assume that you will be asked to create a subclass from the Book class.

class Book:

    def __init__(self, title, author, publisher, page_count, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.page_count = page_count
        self.price = price

    def __str__(self):
        return f"The Title is : {self.title}\n" \
               f"The Author is : {self.author}\n" \
               f"The Publisher is : {self.publisher}\n" \
               f"The Page count is : {self.page_count}\n" \
               f"The price is : {self.price}"

    def get_title(self, title):
        check = input('Search for the title of the book you are looking for')
        if check == title:
            print('Your title has been found')
        else:
            pass
        
    def get_author(self, author):
        check = input('Search for the author you are looking for')
        if check == author:
            print('The author has been found')
        else:
            pass
