# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:57:37 2023

@author: talin
"""

class Person:
    x=1 #class variable, shared between all instances. inside the class can be accesed by self.x OR Person.x
    def __init__(self, name,age,sex,accept,accept1):#these are local parameters while self.name is an object instance. init is executed upon object instantiated
        self.age=age #everytime a variable is called it should look like self.variableName
        self.name=name
        self.sex=sex
        self._accept=accept# the _: not public but when called can be used
        self.__accept2=accept1#the __: it's not public and can't be called
    @property # get property
    def age(self):
        return self._age # note that the age is a private attribute now
    @age.setter # set property
    def age(self,newAge): #name of function is the target attribute
        if 20<newAge<80:
            self._age=newAge
        else:
            raise ValueError("Age should be between 20 and 80")
    def display(self):#instance method
        print("My name is "+self.name)
    def greet(self):#self identifies object that called the method
        print("Hello")
        self.display()#inside the class methods are called through self but outside they are called through the object
    @classmethod
    def method(cls): #just like self cls (class) should be in every class method wich only can affect class variables
        print(cls.x)#cls points to the class itself
    @staticmethod #static methods don't use class varibles or instance variables
    def method1(m,n):
        return m+n
p1=Person("Talin",23,"Female",True,False)#initiation/creation of an object
p1.greet()
Person.method()
# accesing class variables: Person.x OR p1.x OR p2.x

"""
Uses of Properties:
    1. data validation for existing instance attributes.
    2. set an attribute to read only--> creating only get method.
        set an attribute to write only--> creating only set method.
    3. update attributes that depend on other attriputes without turning them into a method.    
"""
"""
# Course exercise:
    
#Exercise 1:
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        print("the name is "+self.name+" the balance is "+str( self.balance))
    def withdraw(self,amount):
        self.balance-=amount
        self.display()
    def deposit(self,amount):
        self.balance+=amount
        self.display()
p1=Bank()
p1.set_details("Talin",100)
p1.deposit(50)
p1.withdraw(50)

#Exercise 2:
class Book:
    def __init__(self,isbn,title,auther,publisher,pages,price,copies):
        self.isbn=isbn
        self.title=title
        self.auther=auther
        self.publisher=publisher
        self.pages=pages
        self.price=price
        self.copies=copies
    def display(self):
        print("The book's isbn is "+self.isbn+", it's title: "+self.title
              +". It's price:"+str(self.price)+", and the number of copies are:"+str(self.copies ))
    def in_stock(self):
        return self.copies>0
    def sell(self):
        if self.in_stock():
            self.copies-=1
            print("remained copies:"+str(self.copies))
        else:
            print("The book is out of stock")
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,enteredPrice):
        if 50<enteredPrice<1000:
            self._price=enteredPrice
        else:
            raise ValueError("the price must be between 50 and 1000")
            
book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)
books=[book1,book2,book3,book4]
for book in books:# display 4 instances of books
    book.display() 
jackBooks=[book.title for book in books if book.auther=="Jack"] #list of books writeen by jack

#Exercise 3
class Fraction:
    def __init__(self,nr,dr):
        self.nr=nr
        self.dr=dr
        if dr<0 and nr<0:
            self.dr=abs(dr)
            self.nr=abs(nr)
        elif dr<0 and nr>0:
            self.dr=dr
            self.nr=-nr
    def show(self):
        print(str(self.nr)+"/"+str(self.dr))
    def multiply(self,other):
        if isinstance(other,int): #examines if other is an integer
          other=Fraction(other,1)# by that if other is an integer the process cam be done
        result=Fraction(self.nr*other.nr, self.dr*other.dr)
        return result
    def add(self,other):
        if isinstance(other,int): #examines if other is an integer
            other=Fraction(other,1)# by that if other is an integer the process cam be done
        result=Fraction(self.nr*other.dr+other.nr*self.dr, self.dr*other.dr)
        return result 

#Exercise 4
class Product:
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount
    
    def display(self):
        print(self.id,  self.marked_price,  self.discount)
    @property
    def selling_price(self):
        self._selling_price=self.marked_price-(self.marked_price*(self.discount/100))
        return self._selling_price
    @property
    def discount(self):
        return self._discount+2 if self.marked_price > 500 else self._discount
 
    @discount.setter
    def discount(self, new_discount):
        self._discount = new_discount
p1 = Product('X879', 400, 6)
print (p1.selling_price)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
print(p3.discount)
p4 = Product('H456', 800, 6)

#Exercise 5
class Circle:
    def __init__(self,radius):
        self._radius=radius

    def area(self):
        return 3.14*(self._radius)**2
    
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,newRadius):
        if newRadius>0:
            self._radius=newRadius
        else:
            raise ValueError("Rdius can't be a negative number")
    @property
    def diameter(self):# properties can be about variables and not attributes
        return 2*self._radius
    @property
    def circumference(self):
        return 2*3.14*self._radius
""" 

       
    
    
