# This code was written by Nandkishor Motiram Dhawale, PhD in June 2022
# This code is written as a learning tutorial in Python Programming language
# The resources was from https://www.tutorialspoint.com/python/index.htm#

# Commenting & Formatting

# item_one = 1
# item_two = 2
# item_three = 3
# total = item_one + \
#         item_two + \
#         item_three
# print(total)
#
# word = 'word'
# sentence = "This is a sentence."
# paragraph = """This is a paragraph. It is
# made up of multiple lines and sentences."""
#
# print(word)
# print(sentence)
# print(paragraph)

# numbers

# import sys
# x = 'foo'
# sys.stdout.write(x + '\n')
#
# counter = 100          # An integer assignment
# miles   = 1000.0       # A floating point
# name    = "John"       # A string
#
# print (counter)
# print (miles)
# print (name)
#
# a = b = c = 1
# print("a", "=", "b", "=", "c", "=", a)
#
# a,b,c = 1,2,"john"
# print (a,b,c)
#
# c = 9.322e-36j
# print(c)
#
# # Strings
# str = 'Hello World!'
#
# print (str)          # Prints complete string
# print (str[0])      # Prints first character of the string
# print (str[2:5])    # Prints characters starting from 3rd to 5th
# print (str[2:])    # Prints string starting from 3rd character
# print (str * 2)     # Prints string two times
# print (str + "TEST") # Prints concatenated string

#List

# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
#
# print (list)         # Prints complete list
# print (list[0])       # Prints first element of the list
# print (list[1:3])     # Prints elements starting from 2nd till 3rd
# print (list[2:])      # Prints elements starting from 3rd element
# print (tinylist * 2)  # Prints list two times
# print (list + tinylist) # Prints concatenated lists

#Tuple
#
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# tinytuple = (123, 'john')
#
# print (tuple)               # Prints the complete tuple
# print (tuple[0])          # Prints first element of the tuple
# print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd
# print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
# print (tinytuple * 2)       # Prints the contents of the tuple twice
# print (tuple + tinytuple)   # Prints concatenated tuples
#
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
# #tuple[2] = 1000    # Invalid syntax with tuple
# list[2] = 1000     # Valid syntax with list
# print(list)
# print(tuple)

#Dictionary

# dict = {}
# dict['one'] = "This is one"
# dict[2]     = "This is two"
#
# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
#
#
# print (dict['one'])      # Prints value for 'one' key
# print (dict[2])           # Prints value for 2 key
# print (tinydict)          # Prints complete dictionary
# print (tinydict.keys())   # Prints all the keys
# print (tinydict.values()) # Prints all the values

# Operators

# print (oct(10))
# print(ord('a'))
#
# a = 21
# b = 10
# c = 0
#
# c = a + b
# print ("Line 1 - Value of c is ", c)
#
# c = a - b
# print ("Line 2 - Value of c is ", c)
#
# c = a * b
# print ("Line 3 - Value of c is ", c)
#
# c = a / b
# print ("Line 4 - Value of c is ", c)
#
# c = a % b
# print ("Line 5 - Value of c is ", c)
#
# a = 2
# b = 3
# c = a**b
# print ("Line 6 - Value of c is ", c)
#
# a = 10
# b = 5
# c = a//b
# print ("Line 7 - Value of c is ", c)
#
#
# a = 21
# b = 10
# c = 0
#
# if ( a == b ):
#    print ("Line 1 - a is equal to b")
# else:
#    print ("Line 1 - a is not equal to b")
#
# if ( a != b ):
#    print ("Line 2 - a is not equal to b")
# else:
#    print ("Line 2 - a is equal to b")
#
# if ( a < b ):
#    print ("Line 4 - a is less than b" )
# else:
#    print ("Line 4 - a is not less than b")
#
# if ( a > b ):
#    print ("Line 5 - a is greater than b")
# else:
#    print ("Line 5 - a is not greater than b")
#
# a = 5;
# b = 20;
# if ( a <= b ):
#    print ("Line 6 - a is either less than or equal to  b")
# else:
#    print ("Line 6 - a is neither less than nor equal to  b")
#
# if ( b >= a ):
#    print ("Line 7 - b is either greater than  or equal to b")
# else:
#    print ("Line 7 - b is neither greater than  nor equal to b")
#
# a = 21
# b = 10
# c = 0
#
# c = a + b
# print ("Line 1 - Value of c is ", c)
#
# c += a
# print ("Line 2 - Value of c is ", c)
#
# c *= a
# print ("Line 3 - Value of c is ", c)
#
# c /= a
# print ("Line 4 - Value of c is ", c)
#
# c = 2
# c %= a
# print ("Line 5 - Value of c is ", c)
#
# c **= a
# print ("Line 6 - Value of c is ", c)
#
# c //= a
# print ("Line 7 - Value of c is ", c)
#
# a = 60  # 60 = 0011 1100
# b = 13  # 13 = 0000 1101
# c = 0
#
# c = a & b  # 12 = 0000 1100
# print("Line 1 - Value of c is ", c)
#
# c = a | b  # 61 = 0011 1101
# print("Line 2 - Value of c is ", c)
#
# c = a ^ b  # 49 = 0011 0001
# print("Line 3 - Value of c is ", c)
#
# c = ~a  # -61 = 1100 0011
# print("Line 4 - Value of c is ", c)
#
# c = a << 2  # 240 = 1111 0000
# print("Line 5 - Value of c is ", c)
#
# c = a >> 2  # 15 = 0000 1111
# print("Line 6 - Value of c is ", c)

# Condition testing

# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ];
#
# if ( a in list ):
#     print ("Line 1 - a is available in the given list")
# else:
#    print ("Line 1 - a is not available in the given list")
#
# if ( b not in list ):
#    print ("Line 2 - b is not available in the given list")
# else:
#    print ("Line 2 - b is available in the given list")
#
# a = 2
# if ( a in list ):
#    print ("Line 3 - a is available in the given list")
# else:
#    print ("Line 3 - a is not available in the given list")
#
#
# a = 20
# b = 20
#
# if ( a is b ):
#    print ("Line 1 - a and b have same identity")
# else:
#    print ("Line 1 - a and b do not have same identity")
#
# if ( id(a) == id(b) ):
#     print ("Line 2 - a and b have same identity")
# else:
#    print ("Line 2 - a and b do not have same identity")
#
# b = 30
# if ( a is b ):
#    print ("Line 3 - a and b have same identity")
# else:
#    print ("Line 3 - a and b do not have same identity")
#
# if ( a is not b ):
#    print ("Line 4 - a and b do not have same identity")
# else:
#    print ("Line 4 - a and b have same identity")
#
#
# var = 100
# if ( var == 100 ) :
#     print ("Value of expression is 100")
# print ("Good bye!")
#
# var1 = 100
# if var1:
#    print ("1 - Got a true expression value")
#    print (var1)
#
# var2 = 1
# if var2:
#    print ("2 - Got a true expression value")
#    print (var2)
# print ("Good bye!")
#
# var1 = 100
# if var1:
#    print ("1 - Got a true expression value")
#    print (var1)
# else:
#    print ("1 - Got a false expression value")
#    print (var1)
#
# var2 = 0
# if var2:
#    print ("2 - Got a true expression value")
#    print (var2)
# else:
#    print ("2 - Got a false expression value")
#    print (var2)
#
# print ("Good bye!")
#
#
# var = 201
# if var < 200:
#    print ("Expression value is less than 200")
#    if var == 150:
#       print ("Which is 150")
#    elif var == 100:
#       print ("Which is 100")
#    elif var == 50:
#       print ("Which is 50")
#    elif var < 50:
#       print ("Expression value is less than 50")
# else:
#    print ("Could not find true expression")
#
# print ("Good bye!")

#Loops

# count = 0
# while (count < 9):
#    print ('The count is:', count)
#    count = count + 1
#
# print ("Good bye!")
#
# for letter in 'Python':     # First Example
#    print ('Current Letter :', letter)
#
# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        # Second Example
#    print ('Current fruit :', fruit)
#
# print ("Good bye!")
#
# i = 2
# while(i < 100):
#    j = 2
#    while(j <= (i/j)):
#       if not(i%j): break
#       j = j + 1
#    if (j > i/j) : print (i, " is prime")
#    i = i + 1
#
# print ("Good bye!")

# Numbers
#
# print ("My name is %s and weight is %d kg!" % ('Zara', 21))
#
# import math
# #numbers
# print ("abs(-45) : ", abs(-45))
# print ("abs(100.12) : ", abs(100.12))
# print ("abs(119L) : ", abs(119))
#
# print ("math.ceil(-45.17) : ", math.ceil(-45.17))
# print ("math.ceil(100.12) : ", math.ceil(100.12))
# print ("math.ceil(100.72) : ", math.ceil(100.72))
# print ("math.ceil(119L) : ", math.ceil(119))
# print ("math.ceil(math.pi) : ", math.ceil(math.pi))
#
# print ("math.exp(-45.17) : ", math.exp(-45.17))
# print ("math.exp(100.12) : ", math.exp(100.12))
# print ("math.exp(100.72) : ", math.exp(100.72))
# print ("math.exp(119L) : ", math.exp(119))
# print ("math.exp(math.pi) : ", math.exp(math.pi))
#
# print ("math.fabs(-45.17) : ", math.fabs(-45.17))
# print ("math.fabs(100.12) : ", math.fabs(100.12))
# print ("math.fabs(100.72) : ", math.fabs(100.72))
# print ("math.fabs(119L) : ", math.fabs(119))
# print ("math.fabs(math.pi) : ", math.fabs(math.pi))
#
# print ("hypot(4, 3) : ",  math.hypot(4, 3))
# print ("hypot(-3, 3) : ",  math.hypot(-3, 3))
# print ("hypot(5, 12) : ",  math.hypot(5, 12))
#
# import random
# import math
#
# print ("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
# print ("choice('A String') : ", random.choice('A String'))
#
# # Select an even number in 100 <= number < 1000
# print ("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))
#
# # Select another number in 100 <= number < 1000
# print ("randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3))
#
# # First random number
# print ("random() : ", random.random())
#
# # Second random number
# print ("random() : ", random.random())
#
# random.seed( 10 )
# print ("Random number with seed 10 : ", random.random())
#
# # It will generate same random number
# random.seed( 10 )
# print ("Random number with seed 10 : ", random.random())
#
# # It will generate same random number
# random.seed( 11 )
# print ("Random number with seed 10 : ", random.random())
#
# # It will generate same random number
# random.seed( 11 )
# print ("Random number with seed 10 : ", random.random())
#
# list = [20, 16, 10, 5];
# random.shuffle(list)
# print ("Reshuffled list : ",  list)
#
# random.shuffle(list)
# print ("Reshuffled list : ",  list)
#
# print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10))
# print ("Random Float uniform(7, 14) : ",  random.uniform(7, 14))
#
# print (math.sin(3))
# print (math.asin(0.1411200080598672))

# Strings

# var1 = 'Hello World!'
# print("Original String : -", var1)
# print ("Updated String :- ", var1[:6] + 'Python')
# print("how r u?",'\a', "i am fine", '\v','\b', "where r u?", '\t', "I am here only", '\r')
#
# a = 'Hello'; b = 'Python'
# print(a+b); print(a*2); print(a[1]); print(b[1:3]); print('P' not in b)
# print ('\n');print ('\n')
# print (r'\n');print (R'\n')
# print ("My name is %s and weight is %g kg!" % ('Zara', 21))
#
# print (r'C:\\nowhere')
#
# str = "this is string example....wow!!!";
# print ("str.capitalize() : ", str.capitalize())
#
# str = "this is string example....wow!!!"
# print ("str.center(60, 'a') : ", str.center(60, 'a'))
#
# str = "this is string example....wow!!!";
#
# sub = "i";
# print ("str.count(sub, 0, 33) : ", str.count(sub, 0, 33))
# sub = "wow";
# print ("str.count(sub) : ", str.count(sub))
#
# str = "this is string example....wow!!!";
# suffix = "wow!!!";
# print (str.endswith(suffix))
# print (str.endswith(suffix,20))
#
# suffix = "is";
# print (str.endswith(suffix, 2, 4))
# print (str.endswith(suffix, 2, 6))
#
# str = "this is string example....wow!!! this is really string"
# print (str.replace("is", "was"))
# print (str.replace("is", "was", 4))
#
# # List, Tuples and Directories
# aList = ['BpamN1', 'Apamn2', 'CPAMM3!'];
# print(aList[2:]); print(aList[1:]); print(aList[0:]);
# print(aList[1]);print(aList[-1]); print(aList[-2]); print(aList[0])
# print ("List Before Reverse: ", aList)
# aList.reverse()
# print ("List After Reverse : ", aList)
# aList.sort();
# print ("List After Sort : ", aList)
#
# tup1 = ('physics', 'chemistry', 1997, 2000);
# tup2 = (1, 2, 3, 4, 5, 6, 7 );
# print ("tup1[0]: ", tup1[0]);
# print ("tup2[1:5]: ", tup2[1:5]);
#
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print ("dict['Name']: ", dict['Name'])
# print ("dict['Age']: ", dict['Age'])
#
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8; # update existing entry
# dict['School'] = "DPS School"; # Add new entry
#
# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])
# print(dict)
# print ("Value : %s" %  dict.values())
# print ("Value : %s" %  dict.keys())


#Date Time and Calender

# import time;  # This is required to include time module.
# import calendar
#
# ticks = time.time()
# print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
#
# localtime = time.localtime(time.time())
# print ("Local current time :", localtime)
#
# localtime = time.asctime( time.localtime(time.time()) )
# print ("Local current time :", localtime)
#
# cal = calendar.month(2022, 7)
# print ("Here is the calendar:")
# print (cal)
#
# print ("time.altzone %d " % time.altzone)
#
# def procedure():
#   time.sleep(2.5)
#
# #measure process time
# t0 = time.clock()
# procedure()
# print (time.clock(), "seconds process time")
#
# #measure wall time
# t0 = time.time()
# procedure()
# print (time.time() - t0, "seconds wall time")
#
# print ("time.ctime() : %s" % time.ctime())
#
# print ("time.localtime() : %s" % time.localtime())
#
# t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
# secs = time.mktime( t )
# print ("time.mktime(t) : %f" %  secs)
# print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))
#
# variable = calendar.calendar(year,w=2,l=1,c=6)
# print(variable)

#Functions

# # Function definition is here
# def printme(str):
#    "This prints a passed string into this function"
#    print (str)
#    return;
#
# # Now you can call printme function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")
#
# # Function definition is here
# def changeme( mylist ):
#    "This changes a passed list into this function"
#    mylist.append([1,2,3,4]);
#    print ("Values inside the function: ", mylist)
#    return
#
# # Now you can call changeme function
# mylist = [10,20,30];
# changeme( mylist );
# print ("Values outside the function: ", mylist)
#
# # Function definition is here
# def changeme( mylist ):
#    "This changes a passed list into this function"
#    mylist = [1,2,3,4]; # This would assig new reference in mylist
#    print ("Values inside the function: ", mylist)
#    return
#
# # Now you can call changeme function
# mylist = [10,20,30];
# changeme( mylist );
# print ("Values outside the function: ", mylist)
#
#
# # Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print (str)
#    return;
#
# # Now you can call printme function
# printme( str = "My string")
#
# # Function definition is here
# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return;
#
# # Now you can call printinfo function
# printinfo( age=50, name="miki" )
#
# # Function definition is here
# def printinfo( name, age = 35 ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return;
#
# # Now you can call printinfo function
# printinfo( age=50, name="miki" )
# printinfo( name="miki" )
#
# # Function definition is here
# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print ("Output is: ")
#    print (arg1)
#    for var in vartuple:
#       print (var)
#    return;
#
# # Now you can call printinfo function
# printinfo( 10 )
# printinfo( 70, 60, 50 )
#
# # Function definition is here
# sum = lambda arg1, arg2: arg1 + arg2;
#
# # Now you can call sum as a function
# print ("Value of total : ", sum( 10, 20 ))
# print ("Value of total : ", sum( 20, 20 ))
#
# # Function definition is here
# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    total = arg1 + arg2
#    print ("Inside the function : ", total)
#    return total;
#
# # Now you can call sum function
# total = sum( 10, 20 );
# print ("Outside the function : ", total)
#
# total = 0; # This is global variable.
# # Function definition is here
# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    total = arg1 + arg2; # Here total is local variable.
#    print ("Inside the function local total : ", total)
#    return total;
#
# # Now you can call sum function
# sum( 10, 20 );
# print ("Outside the function global total : ", total)

#Modules


# IO

# str = input("Enter your input: ")
# print ("Received input is : ", str)
#
# #Open a file
# fo = open("foo.txt", "wb")
# print ("Name of the file: ", fo.name)
# print ("Closed or not : ", fo.closed)
# print ("Opening mode : ", fo.mode)
# # print ("Softspace flag : ", fo.softspace)
#
# # Close opend file
# fo.close()
#
# # Open a file
# fo = open("foo.txt", "w")
# fo.write( "Python is a great language.\nYeah its great!!\n")
#
# # Close opend file
# fo.close()
#
# # Open a file
# fo = open("foo.txt", "r+")
# str = fo.read(45);
# print ("Read String is : ", str)
# # Close opend file
# fo.close()
#
# #Open a file
# fo = open("foo.txt", "r+")
# str = fo.read(22)
# print ("Read String is : ", str)
#
# # Check current position
# position = fo.tell()
# print ("Current file position : ", position)
#
# # Reposition pointer at the beginning once again
# position = fo.seek(22, 0);
# str = fo.read(22)
# print ("Again read String is : ", str)
# # Close opend file
# fo.close()

# Exceptions

# import unittest
# def KelvinToFahrenheit(Temperature):
#    assert (Temperature >= 0),"Colder than absolute zero!"
#    return ((Temperature-273)*1.8)+32
#
# print (KelvinToFahrenheit(273))
# print (int(KelvinToFahrenheit(505.78)))
# print (KelvinToFahrenheit(-5))
#
# try:
#    fh = open("testfile", "w")
#    fh.write("This is my test file for exception handling!!")
# except IOError:
#    print ("Error: can\'t find file or read data")
# else:
#    print ("Written content in the file successfully")
#    fh.close()
#
# try:
#    fh = open("testfile", "w")
#    try:
#       fh.write("This is my test file for exception handling!!")
#    finally:
#       print ("Going to close the file")
#       fh.close()
# except IOError:
#    print ("Error: can\'t find file or read data")
#
# #Define a function here.
# def temp_convert(var):
#    try:
#       return int(var)
#    except ValueError as Argument:
#       print ("The argument does not contain numbers\n", Argument);
#       return;
#
# # Call above function here.
# temp_convert("xyz")
#
# class Networkerror(RuntimeError):
#     def __init__(self, arg):
#       self.args = arg
# try:
#    raise Networkerror("Bad hostname")
# except Networkerror as e:
#    print (e.args)

# Class in Python

# class Employee: # Define a Class (Employee is an object)
#     "Common base class for all employees"
#     empCount = 0 #Define a Class variable (inside the class but outside the class methods)
#
#     def __init__(self, name, salary, age): #class constructor or initialization method that Python calls when you create a new instance of this class.
#         self.name = name #instance variable
#         self.salary = salary #instance variable
#         self.age = age  # instance variable
#         Employee.empCount += 1 #instance variable
#
#     def displayCount(self): #other class methods like normal functions with the exception that the first argument to each method is self.
#         print ("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self): #other class methods like normal functions with the exception that the first argument to each method is self.
#         print ("Name : ", self.name, ", Salary: ", self.salary, ", Age: ", self.age)
#
# emp1 = Employee("Sitara", 2000, 21) #This would create first object of Employee class with attributes
# emp2 = Employee("Shani", 5000, 25) #This would create next object of Employee class with attributes
#
# emp1.displayEmployee() #call class method
# emp2.displayEmployee()#call class method
# emp2.displayCount()#call class method
#
# emp1.age = 25 # Modify 'age' attribute.
# emp2.age = 21 # Modify 'age' attribute.
#
# emp1.name = "Mitushi" # Modify 'age' attribute.
# emp2.name = "Takishi" # Modify 'age' attribute.
#
# emp1.displayEmployee()#call class method
# emp2.displayEmployee()#call class method
#
# print ("Employee.__doc__:", Employee.__doc__)
# print ("Employee.__name__:", Employee.__name__)
# print ("Employee.__module__:", Employee.__module__)
# print ("Employee.__bases__:", Employee.__bases__)
# print ("Employee.__dict__:", Employee.__dict__)
#
# hasattr(emp1, 'age') # Returns true if 'age' attribute exists
# getattr(emp1, 'age') # Returns value of 'age' attribute
# setattr(emp1, 'age', 8) # Set attribute 'age' at 8
# # delattr(emp1, 'age') # Delete attribute 'age'
# emp1.displayEmployee()#call class method
#
# # destructor
# class Point:
#    def __init__( self, x=0, y=0): #constructor
#       self.x = x
#       self.y = y
#    def __del__(self): #destructor
#       class_name = self.__class__.__name__
#       print (class_name, "destroyed")
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print (id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts
# del pt1
# del pt2
# del pt3
#
# #inheritance
# class Parent:        # define parent class
#    parentAttr = 100
#    def __init__(self):
#       print ("Calling parent constructor")
#
#    def parentMethod(self):
#       print ('Calling parent method')
#
#    def setAttr(self, attr):
#       Parent.parentAttr = attr
#
#    def getAttr(self):
#       print ("Parent attribute :", Parent.parentAttr)
#
# class Child(Parent): # define child class
#    def __init__(self):
#       print ("Calling child constructor")
#
#    def childMethod(self):
#       print ('Calling child method')
#
# c = Child()          # instance of child
# c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(200)       # again call parent's method
# c.getAttr()          # again call parent's method
#
# #Overriding Methods
# class Parent:        # define parent class
#    def myMethod(self):
#       print ('Calling parent method')
#
# class Child(Parent): # define child class
#    def myMethod(self):
#       print ('Calling child method')
#
# c = Child()          # instance of child
# c.myMethod()         # child calls overridden method
#
# # Overloading Operators
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print (v1 + v2)
#
# # Data Hiding
# class JustCounter:
#     __secretCount = 0
#
#     def count(self):
#         self.__secretCount += 1
#         print (self.__secretCount)
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print (counter._JustCounter__secretCount)
# print(counter.__secretCount)

# Reg Expressions

# import re
#
# line = "Cats are smarter than dogs"
#
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print ("No match!!")
#
# import re
#
# line = "Cats are smarter than dogs";
#
# matchObj = re.match( r'Cats', line, re.M|re.I)
# if matchObj:
#    print ("match --> matchObj.group() : ", matchObj.group())
# else:
#    print ("No match!!")
#
# searchObj = re.search(r'dogs', line, re.M|re.I)
# if searchObj:
#    print ("search --> searchObj.group() : ", searchObj.group())
# else:
#    print ("Nothing found!!")
#
# import re
#
# phone = "2004-959-559 # This is Phone Number"
#
# # Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# print ("Phone Num : ", num)
#
# # Remove anything other than digits
# num = re.sub(r'\D', "", phone)
# print ("Phone Num : ", num)

#Email

# import smtplib
#
# sender = 'nmdhawale@gmail.com'
# receivers = ['drnmdhawale@gmail.com']
#
# message = """From: From Person <nmdhawale@gmail.com>
# To: To Person <rnmdhawale@gmail.com>
# Subject: SMTP e-mail test
# This is a test e-mail message.
# """
# try:
#    #smtpObj = smtplib.SMTP('localhost')
#    smtpObj = smtplib.SMTP('mail.gmail.com', 25)
#    smtpObj.sendmail(sender, receivers, message)
#    print ("Successfully sent email")
# except SMTPException:
#    print ("Error: unable to send email")

# XML Parser

#SAX

# import xml.sax
# class MovieHandler(xml.sax.ContentHandler):
#     def __init__(self):
#         self.CurrentData = ""
#         self.type = ""
#         self.format = ""
#         self.year = ""
#         self.rating = ""
#         self.stars = ""
#         self.description = ""
#
#     # Call when an element starts
#     def startElement(self, tag, attributes):
#         self.CurrentData = tag
#         if tag == "movie":
#             print
#             "*****Movie*****"
#             title = attributes["title"]
#             print
#             "Title:", title
#
#     # Call when an elements ends
#     def endElement(self, tag):
#         if self.CurrentData == "type":
#             print
#             "Type:", self.type
#         elif self.CurrentData == "format":
#             print
#             "Format:", self.format
#         elif self.CurrentData == "year":
#             print
#             "Year:", self.year
#         elif self.CurrentData == "rating":
#             print
#             "Rating:", self.rating
#         elif self.CurrentData == "stars":
#             print
#             "Stars:", self.stars
#         elif self.CurrentData == "description":
#             print
#             "Description:", self.description
#         self.CurrentData = ""
#
#     # Call when a character is read
#     def characters(self, content):
#         if self.CurrentData == "type":
#             self.type = content
#         elif self.CurrentData == "format":
#             self.format = content
#         elif self.CurrentData == "year":
#             self.year = content
#         elif self.CurrentData == "rating":
#             self.rating = content
#         elif self.CurrentData == "stars":
#             self.stars = content
#         elif self.CurrentData == "description":
#             self.description = content
#
#
# if (__name__ == "__main__"):
#     # create an XMLReader
#     parser = xml.sax.make_parser()
#     # turn off namepsaces
#     parser.setFeature(xml.sax.handler.feature_namespaces, 0)
#
#     # override the default ContextHandler
#     Handler = MovieHandler()
#     parser.setContentHandler(Handler)
#
#     parser.parse("movies.xml")

# DOM

# from xml.dom.minidom import parse
# import xml.dom.minidom
#
# # Open XML document using minidom parser
# DOMTree = xml.dom.minidom.parse("movies.xml")
# collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print ("Root element : %s" % collection.getAttribute("shelf"))
#
# # Get all the movies in the collection
# movies = collection.getElementsByTagName("movie")
#
# # Print detail of each movie.
# for movie in movies:
#    print ("*****Movie*****")
#    if movie.hasAttribute("title"):
#       print ("Title: %s" % movie.getAttribute("title"))
#
#    type = movie.getElementsByTagName('type')[0]
#    print ("Type: %s" % type.childNodes[0].data)
#    format = movie.getElementsByTagName('format')[0]
#    print ("Format: %s" % format.childNodes[0].data)
#    rating = movie.getElementsByTagName('rating')[0]
#    print ("Rating: %s" % rating.childNodes[0].data)
#    description = movie.getElementsByTagName('description')[0]
#    print ("Description: %s" % description.childNodes[0].data)

#Python - GUI Programming (Tkinter)

# from tkinter import *
# import tkinter
# import tkinter.messagebox
#
# top = tkinter.Tk()
#
# C = tkinter.Canvas(top, bg="blue", height=250, width=300)
#
# coord = 10, 50, 240, 210
# arc = C.create_arc(coord, start=0, extent=150, fill="red")
#
# def helloCallBack():
#    tkinter.messagebox.showinfo( "Hello Python", "Hello World")
#
# B = tkinter.Button(top, text ="Hello", command = helloCallBack)
#
# CheckVar1 = IntVar()
# CheckVar2 = IntVar()
# C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
#                  onvalue = 1, offvalue = 0, height=5, \
#                  width = 20)
# C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
#                  onvalue = 1, offvalue = 0, height=5, \
#                  width = 20)
#
# L1 = Label(top, text="User Name")
# E1 = Entry(top, bd =5)
# L1.pack( side = LEFT)
# E1.pack(side = RIGHT)
#
# C1.pack()
# C2.pack()
# C.pack()
# B.pack()
# top.mainloop()

# from tkinter import *
# root = Tk()
# frame = Frame(root)
# frame.pack()
#
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
#
# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)
#
# greenbutton = Button(frame, text="Brown", fg="brown")
# greenbutton.pack( side = LEFT )
#
# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )
#
# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)
#
# var = StringVar()
# label = Label( root, textvariable=var, relief=RAISED )
#
# var.set("Hey!? How are you doing?")
# label.pack()
#
# root.mainloop()

# List Box

# from tkinter import *
# import tkinter.messagebox
# import tkinter
#
# top = Tk()
#
# Lb1 = Listbox(top)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")
#
# Lb1.pack()
# top.mainloop()

#Python - Tkinter Menubutton

# from tkinter import *
# import tkinter.messagebox
# import tkinter
#
# top = Tk()
#
# mb=  Menubutton ( top, text="condiments", relief=RAISED )
# mb.grid()
# mb.menu =  Menu ( mb, tearoff = 0 )
# mb["menu"] =  mb.menu
#
# mayoVar = IntVar()
# ketchVar = IntVar()
#
# mb.menu.add_checkbutton ( label="mayo",
#                           variable=mayoVar )
# mb.menu.add_checkbutton ( label="ketchup",
#                           variable=ketchVar )
#
# mb.pack()
# top.mainloop()

#Python - Tkinter Menu

# from tkinter import *
# def donothing():
#     filewin = Toplevel(root)
#     button = Button(filewin, text="Do nothing button")
#     button.pack()
#
# root = Tk()
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)
#
# filemenu.add_separator()
#
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)
#
# editmenu.add_separator()
#
# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)
#
# menubar.add_cascade(label="Edit", menu=editmenu)
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="Help Index", command=donothing)
# helpmenu.add_command(label="About...", command=donothing)
# menubar.add_cascade(label="Help", menu=helpmenu)
#
# root.config(menu=menubar)
# root.mainloop()


#Python - Tkinter Message

# from tkinter import *
#
# root = Tk()
# var = StringVar()
# label = Message( root, textvariable=var, relief=RAISED )
#
# var.set("Hey!? How are you doing?")
# label.pack()
# root.mainloop()

#Python - Tkinter Radiobutton

# from tkinter import *
#
# def sel():
#    selection = "You selected the option " + str(var.get())
#    label.config(text = selection)
#
# root = Tk()
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
#                   command=sel)
# R1.pack( anchor = W )
#
# R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
#                   command=sel)
# R2.pack( anchor = W )
#
# R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
#                   command=sel)
# R3.pack( anchor = W)
#
# label = Label(root)
# label.pack()
# root.mainloop()

#Python - Tkinter Scale

# from tkinter import *
#
# def sel():
#    selection = "Value = " + str(var.get())
#    label.config(text = selection)
#
# root = Tk()
# var = DoubleVar()
# scale = Scale( root, variable = var )
# scale.pack(anchor=CENTER)
#
# button = Button(root, text="Get Scale Value", command=sel)
# button.pack(anchor=CENTER)
#
# label = Label(root)
# label.pack()
#
# root.mainloop()

#Python - Tkinter Scrollbar

# from tkinter import *
#
# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )
#
# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, "This is line number " + str(line))
#
# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )
#
# mainloop()

#Python - Tkinter Text

# from tkinter import *
#
# def onclick():
#    pass
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack()
#
# text.tag_add("here", "1.0", "1.4")
# text.tag_add("start", "1.8", "1.13")
# text.tag_config("here", background="yellow", foreground="blue")
# text.tag_config("start", background="black", foreground="green")
# root.mainloop()

#Python - Tkinter Toplevel

# from tkinter import *
#
# root = Tk()
# top = Toplevel()
# top.mainloop()

#Python - Tkinter Spinbox

# from tkinter import *
#
# master = Tk()
#
# w = Spinbox(master, from_=0, to=10)
# w.pack()
#
# mainloop()

#Python - Tkinter PanedWindow

# from tkinter import *
#
# m1 = PanedWindow()
# m1.pack(fill=BOTH, expand=1)
#
# left = Label(m1, text="left pane")
# m1.add(left)
#
# m2 = PanedWindow(m1, orient=VERTICAL)
# m1.add(m2)
#
# top = Label(m2, text="top pane")
# m2.add(top)
#
# bottom = Label(m2, text="bottom pane")
# m2.add(bottom)
#
# mainloop()

#Python - Tkinter LabelFrame

# from tkinter import *
#
# root = Tk()
#
# labelframe = LabelFrame(root, text="This is a LabelFrame")
# labelframe.pack(fill="both", expand="yes")
#
# left = Label(labelframe, text="Inside the LabelFrame")
# left.pack()
#
# root.mainloop()

#Python - Tkinter tkMessageBox

# import tkinter
# import tkinter.messagebox
#
# top = tkinter.Tk()
# def hello():
#    tkinter.messagebox.showinfo("Say Hello", "Hello World")
#
# B1 = tkinter.Button(top, text = "Say Hello", command = hello)
# B1.pack()
#
# top.mainloop()

#Python - Tkinter grid() Method

# import tkinter
# root = tkinter.Tk(  )
# for r in range(3):
#    for c in range(4):
#       tkinter.Label(root, text='R%s/C%s'%(r,c),
#          borderwidth=1 ).grid(row=r,column=c)
# root.mainloop(  )

#Python - Tkinter place() Method

# from tkinter import *
# import tkinter.messagebox
# import tkinter
#
# top = tkinter.Tk()
#
# def helloCallBack():
#    tkinter.messagebox.showinfo( "Hello Python", "Hello World")
#
# B = tkinter.Button(top, text ="Hello", command = helloCallBack)
#
# B.pack()
# B.place(bordermode=OUTSIDE, height=100, width=100)
# top.mainloop()

# #Python - Multithreaded Programming

# import _thread
# import time
# # Define a function for the thread
# def print_time(threadName, delay):
#    count = 0
#    while count < 10:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#
# # Create two threads as follows
# try:
#    _thread.start_new_thread(print_time, ("Thread-1", 1, ))
#    _thread.start_new_thread(print_time, ("Thread-2", 3, ))
# except:
#    print ("Error: unable to start thread")
# while 1:
#    pass

# import threading
# import time
# exitFlag = 0
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, 5, self.counter)
#       print ("Exiting " + self.name)
#
# def print_time(threadName, counter, delay):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1
#       print ("counter is : ", counter)
#
# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
# thread3 = myThread(3, "Thread-3", 3)
#
# # Start new Threads
# thread1.start()
# thread2.start()
# thread3.start()
#
# print ("Exiting Main Thread")

#Synchronizing Threads
#
# import threading
# import time
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       # Get lock to synchronize threads
#       threadLock.acquire()
#       print_time(self.name, self.counter, 3)
#       # Free lock to release next thread
#       threadLock.release()
#
# def print_time(threadName, delay, counter):
#    while counter:
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1
#
# threadLock = threading.Lock()
# threads = []
#
# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
#
# # Add threads to thread list
# threads.append(thread1)
# threads.append(thread2)
#
# # Wait for all threads to complete
# for t in threads:
#     t.join()
# print ("Exiting Main Thread")

#Multithreaded Priority Queue

# import queue
# import threading
# import time
# 
# exitFlag = 0
# 
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, q):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.q = q
#    def run(self):
#       print ("Starting " + self.name)
#       process_data(self.name, self.q)
#       print ("Exiting " + self.name)
# 
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print ("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#             time.sleep(1)
# 
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue =queue.Queue(10)
# threads = []
# threadID = 1
# 
# # Create new threads
# for tName in threadList:
#    thread = myThread(threadID, tName, workQueue)
#    thread.start()
#    threads.append(thread)
#    threadID += 1
# 
# # Fill the queue
# queueLock.acquire()
# for word in nameList:
#    workQueue.put(word)
# queueLock.release()
# 
# # Wait for queue to empty
# while not workQueue.empty():
#    pass
# 
# # Notify threads it's time to exit
# exitFlag = 1
# 
# # Wait for all threads to complete
# for t in threads:
#    t.join()
# print ("Exiting Main Thread")
