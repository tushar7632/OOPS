# A Sample class with init method
# class Person:
 
#     # init method or constructor
#     def __init__(self, name):
#         self.name = name
#         print(self.name)
#     # Sample Method
#     # def say_hi(self):
#     #     print('Hello, my name is', self.name)
 
 
# p = Person('Nikhil')
# # p.say_hi() 


# tushar = Person('ramesh')
# # tushar.say_hi()
# aayush= Person('vicky')
# aayush.say_hi()


# A Sample class with init method
# class Person:
 
#     # init method or constructor
#     def __init__(self, name):
#         self.name = name
 
#     # Sample Method
#     def say_hi(self):
#         print('Hello, my name is', self.name)
 
 
# # Creating different objects
# p1 = Person('Nikhil')
# p2 = Person('Abhinav')
# p3 = Person('Anshul')
 
# p1.say_hi() 
# p2.say_hi()
# p3.say_hi()

# Python program to
# demonstrate init with
# inheritance
 
 
 
# class A:
#     def __init__(self, something):
#         print("A init called")
#         self.something = something
 
 
# class B(A):
#     def __init__(self, something):
#         # Calling init of parent class
#         A.__init__(self, something)
#         print("B init called")
#         self.something = something
 
 
# obj = B("Something")\
           
# def print_Geek(self):
#         print(self.geek)
#         print(self.xyz) 


# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks" 


# # Creating a derived class
# class Derived(Base):
#     def __init__(self):

#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)


# # Driver code
# obj1 = Base()
# print(obj1.a)\  

# class car:
#     colour = "Blue"
#     brand = "mercedes"
    
# car1 = car()
# print(car1.colour)
# print(car1.brand)


# class Student:
    
    
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new student in database..")
    
# s1 = Student("Tushar")
# print(s1.name) #karan

# s2 = Student("kittu")
# print(s2.name)



# class Student:
    
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database..")
    
# s1 = Student("Tushar", 97)
# print(s1.name, s1.marks) #karan

# s2 = Student("kittu", 98)
# print(s2.name, s2.marks)



# class GeekforGeeks:
 
#     # default constructor
#     def __init__(self,fname="hello tushar kaise ho",lname="i am ok"):
#         self.geek = "GeekforGeeks"
#         self.aayush=fname
#         self.tushar=lname
 
#     # a method for printing data members
#     def print_Geek(self):
#         print(self.geek)  #GeekforGeeks
        
        
#     def xyz(self):
#         print(self.aayush)  #
        
#     def abc(self):
#         print(self.tushar) #
 
 
# # creating object of the class
# # obj = GeekforGeeks("ravikumar","mukeshkumar")
# obj = GeekforGeeks()
 
# # calling the instance method using the object obj
# obj.print_Geek()
# obj.xyz()
# obj.abc()





# class Addition:
#     first = 0
#     second = 0
#     answer = 0
 
#     # parameterized constructor
#     def __init__(self, f, s):
#         self.first = f
#         self.second = s
 
#     def display(self):
#         print("First number = " + str(self.first))
#         print("Second number = " + str(self.second))
#         print("Addition of two numbers = " + str(self.answer))
 
#     def calculate(self):
#         self.answer = self.first + self.second
 
 
# # creating object of the class
# # this will invoke parameterized constructor
# obj1 = Addition(1000, 2000)
 
# # perform Addition on obj1
# obj1.calculate()


# # display result of obj1
# obj1.display()
# # creating second object of same class
# obj2 = Addition(10, 20)
 
 
# # perform Addition on obj2
# obj2.calculate()
 
 
# # display result of obj2
# obj2.display()



# class MyClass:
#     def __init__(self, name=None):
#         if name is None:
#             print("Default constructor called")
#         else:
#             self.name = name
#             print("Parameterized constructor called with name", self.name)
     
#     def method(self):
#         if hasattr(self, 'name'):
#             print("Method called with name", self.name)
#         else:
#             print("Method called without a name")
 
# # Create an object of the class using the default constructor
# obj1 = MyClass()
 
# # Call a method of the class
# # obj1.method()
 
# # Create an object of the class using the parameterized constructor
# obj2 = MyClass("John")
 
# # # Call a method of the class
# obj2.method()


# class Student:
    
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database..")
    
# s1 = Student("Tushar", 97)
# print(s1.name, s1.marks) #karan

# s2 = Student("kittu", 98)
# print(s2.name, s2.marks)



# inheritance in python 

# # A Python program to demonstrate inheritance
# class Person:
   
#   # Constructor
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id
 
#   # To check if this person is an employee
#   def Display(self):
#     print(self.name, self.id)
 
 
# # Driver code
# emp = Person("Satyam", 102) # An Object of Person
# emp.Display()

# class Emp(Person):
   
#   def Print(self):
#     print("Emp class called")
     
# Emp_details = Emp("Mayank", 103)
 
# # calling parent class function
# Emp_details.Display()
 
# # Calling child class function
# Emp_details.Print()



# class Abc(Emp):
   
#   def Print(self):
#     print("Abc class called")
     
# Emp_detail = Emp("tushar", 105)
 
# # calling parent class function
# Emp_detail.Display()
 
# # Calling child class function
# Emp_detail.Print()



# class Student:
  
#   #default constructors
#     def __init__(self,):
#       pass
     
#     #parametrized constructor     
         
#     def __init__(xyz, name, marks):
#         xyz.name = name
#         xyz.marks = marks
#         print("I always respect girl")
    
    
# s1 = Student("Tushar", 97)
# del s1.marks
# print(s1.name, s1.marks) #karan

# s2 = Student("kittu", 98)
# print(s2.name, s2.marks)  



# Python code to demonstrate how parent constructors
# are called.
 
# parent class
# class Person:
 
#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
 
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
 
# # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
    
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
        
#     def display2(self):
#         print(self.salary)
#         print(self.post)
 
      
 
# # creation of an object variable or an instance
# a = Employee('Rahul', 886012, 200, "Intern")
 
# # calling a function of the class Person using its instance
# a.display()
# a.display2()



# class A:
#     def __init__(self, n='Rahul'):
#         self.name = n
 
# class B(A):
#     def __init__(self, roll):
#         self.roll = roll
#         A.__init__(self)
 
# object = B(23)
# # print(object.name)
# print(object.roll)
# print(object.name)



# # parent class
# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
 
#   def display(self):
#     print(self.name, self.age)
 
# # child class
# class Student(Person):
#   def __init__(self, name, age):
#     self.sName = name
#     self.sAge = age
#     # inheriting the properties of parent class
#     super().__init__("Rahul", age)
 
#   def displayInfo(self):
#     print(self.sName, self.sAge)
 
# obj = Student("Mayank", 23)
# obj.display()
# obj.displayInfo()



# Python example to show the working of multiple
# inheritance
 
# class Base1(object):
#     def __init__(self):
#         self.str1 = "Geek1"
#         print("Base1")
 
 
# class Base2(object):
#     def __init__(self):
#         self.str2 = "Geek2"
#         print("Base2")
 
 
# class Derived(Base1, Base2):
#     def __init__(self):
 
#         # Calling constructors of Base1
#         # and Base2 classes
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")
 
#     def printStrs(self):
#         print(self.str1, self.str2)
 
 
# ob = Derived()
# ob.printStrs()

# class student:
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print(self.name ,self.marks)
#         #     
        
# s1 = student("Rahul", [98, 99, 77])
# s1.abc()
        
        
        
        # access specifiers in python 
# program to illustrate public access modifier in a class


# class Geek:

#     # constructor
#     def __init__(self, name, age):

#         # public data members
#         self.geekName = name
#         self.geekAge = age

#     # public member function
#     def displayAge(self):

#         # accessing public data member
#         print("Age: ", self.geekAge)


# # creating object of the class
# obj = Geek("R2J", 20)

# # accessing public data member
# print("Name: ", obj.geekName)

# # calling public member function of the class
# obj.displayAge()
        
        
        
        # program to illustrate protected access modifier in a class

# super class


# class Student:

#     # protected data members
#     _name = None
#     _roll = None
#     _branch = None

#     # constructor
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch

#     # protected member function
#     def _displayRollAndBranch(self):

#         # accessing protected data members
#         print("Roll: ", self._roll)
#         print("Branch: ", self._branch)


# # derived class
# class Geek(Student):

#     # constructor
#     def __init__(self, name, roll, branch):
#         Student.__init__(self, name, roll, branch)

#     # public member function
#     def displayDetails(self):

#               # accessing protected data members of super class
#         print("Name: ", self._name)

#         # accessing protected member functions of super class
#         self._displayRollAndBranch()


# # creating objects of the derived class
# obj = Geek("R2J", 1706256, "Information Technology")

# # calling public member functions of the class
# obj.displayDetails()



# class Letslearncoding:
#     def __init__(self):
#         self._name="hello everyone"
#     def _abc(self):
#         print(self._name)
        
# obj = Letslearncoding()
# print(obj._name)
# obj._abc()


# private access specifiers 


# program to illustrate private access modifier in a class


# class Geek:

#     # private members
#     __name = None
#     __roll = None
#     __branch = None

#     # constructor
#     def __init__(self, name, roll, branch):
#         self.__name = name
#         self.__roll = roll
#         self.__branch = branch

#     # private member function
#     def __displayDetails(self):

#         # accessing private data members
#         print("Name: ", self.__name)
#         print("Roll: ", self.__roll)
#         print("Branch: ", self.__branch)

#     # public member function
#     def accessPrivateFunction(self):

#         # accessing private member function
#         self.__displayDetails()


# # creating object
# obj = Geek("R2J", 1706256, "Information Technology")

# # calling public member function of the class
# obj.accessPrivateFunction()

# Polymorphism in Python


# Python program to demonstrate in-built poly-
# morphic functions
 
# len() being used for a string
# print(len("geeks"))
# # len() being used for a list
# print(len([10, 20, 30]))

# A simple Python function to demonstrate 
# Polymorphism
 
# def add(x, y, z = 0): 
#     return x + y+z
 
# # Driver code 
# print(add(2, 3)) #5
# print(add(2, 3, 4)) #9


# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
 
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
 
#     def type(self):
#         print("India is a developing country.")
 
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
 
#     def language(self):
#         print("English is the primary language of USA.")
 
#     def type(self):
#         print("USA is a developed country.")
 
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()



# class Bird:
#   def intro(self):
#     print("There are many types of birds.")
     
#   def flight(self):
#     print("Most of the birds can fly but some cannot.")
   
# class sparrow(Bird):
#   def flight(self):
#     print("Sparrows can fly.")
     
# class ostrich(Bird):
#   def flight(self):
#     print("Ostriches cannot fly.")
     
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
 
# obj_bird.intro()
# obj_bird.flight()
 
# obj_spr.intro()
# obj_spr.flight()
 
# obj_ost.intro()
# obj_ost.flight()



# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
  
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
  
#     def type(self):
#         print("India is a developing country.")
  
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
  
#     def language(self):
#         print("English is the primary language of USA.")
  
#     def type(self):
#         print("USA is a developed country.")

# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
  
# obj_ind = India()
# obj_usa = USA()
  

# func(obj_usa)

# func(obj_ind)





# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method")
 
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
 
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
 
# # Create a list of Animal objects
# animals = [Dog(), Cat()]
 
# # Call the speak method on each object
# for animal in animals:
#     print(animal.speak())


# encapsulation in python 

# Python program to 
# demonstrate protected members 
  
# Creating a base class 
# class Base: 
#     def __init__(self): 
  
#         # Protected member 
#         self._a = 2
  
# # Creating a derived class 
# class Derived(Base): 
#     def __init__(self): 
  
#         # Calling constructor of 
#         # Base class 
#         Base.__init__(self) 
#         print("Calling protected member of base class: ",  
#               self._a) 
  
#         # Modify the protected variable: 
#         self._a = 3
#         print("Calling modified protected member outside class: ", 
#               self._a) 
  
  
# obj1 = Derived() 

# obj2 = Base() 
  
# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 
  
# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 




# Python program to 
# demonstrate private members 
  
# Creating a Base class 
  
  
# class Base: 
#     def __init__(self): 
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks"
  
# # Creating a derived class 
# class Derived(Base): 
#     def __init__(self): 
#         # print("hello everyone")
#         # Calling constructor of 
#         # Base class 
#         Base.__init__(self) 
#         print("Calling private member of base class: ") 
#         print(self.__c) 
# # Driver code 
# obj1 = Derived() 
# print(obj1.__c)
  
# Abstraction

# class car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
        
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")
# car1 = car()
# car1.start()

# #Encapsulation

# class Account:
#         def __init__(self, balance,acc):
#                 self.balance = balance
#                 self.account_no = acc
                
#                 # debit method
#                 def debit(self, amount):
#                         self.balance -= amount
#                         print("Rs.", amount, "was debited")
#                         print("total balance = ", self.get_balance())
                        
#                         def credit(self, credit):
#                                 self.balance += amount
#                         print("Rs.", amount, "was credited")
#                         print("total balance = ", self.get_balance())
#         def get__balance(self):
#                 return self.balance
                        
# acc1 = Account(5000, 1000)
# acc1.debit(1000)
# acc1.credit(500)


class Account:
        def _init_(self, balance,acc):
                self.balance = balance
                self.account_no = acc
                
                # debit method
                def debit(self, amount):
                        self.balance -= amount
                        print("Rs.", amount, "was debited")
                        print("total balance = ", self.get_balance())
                        
                        def credit(self, credit):
                                self.balance += amount
                        print("Rs.", amount, "was credited")
                        print("total balance = ", self.get_balance())
        def get__balance(self):
                return self.balance
                        
acc1 = Account(5000, 1000)
acc1.debit(1000)
acc1.credit(500)
