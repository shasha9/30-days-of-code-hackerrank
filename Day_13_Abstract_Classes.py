#Task
#Given a Book class and a Solution class, write a MyBook class that does the following:
#Inherits from Book
#Has a parameterized constructor taking these  parameters:
#string title
#string author
#int price
#Implements the Book class' abstract display() method so it prints these 3 lines:
#title, a space, and then the current instance's title.
#author, a space, and then the current instance's author .
#price, a space, and then the current instance's price .



#Write MyBook class
class MyBook(Book) :
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price = price
    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))
