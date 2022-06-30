
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total)

word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

print(word)
print(sentence)
print(paragraph)

import sys
x = 'foo'
sys.stdout.write(x + '\n')

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter)
print (miles)
print (name)

a = b = c = 1
print("a", "=", "b", "=", "c", "=", a)

a,b,c = 1,2,"john"
print (a,b,c)

c = 9.322e-36j
print(c)

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])      # Prints first character of the string
print (str[2:5])    # Prints characters starting from 3rd to 5th
print (str[2:])    # Prints string starting from 3rd character
print (str * 2)     # Prints string two times
print (str + "TEST") # Prints concatenated string

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)         # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])          # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list
print(list)
print(tuple)

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])      # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

print (oct(10))
print(ord('a'))

a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c = a - b
print ("Line 2 - Value of c is ", c)

c = a * b
print ("Line 3 - Value of c is ", c)

c = a / b
print ("Line 4 - Value of c is ", c)

c = a % b
print ("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b
print ("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b
print ("Line 7 - Value of c is ", c)


a = 21
b = 10
c = 0

if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")

if ( a < b ):
   print ("Line 4 - a is less than b" )
else:
   print ("Line 4 - a is not less than b")

if ( a > b ):
   print ("Line 5 - a is greater than b")
else:
   print ("Line 5 - a is not greater than b")

a = 5;
b = 20;
if ( a <= b ):
   print ("Line 6 - a is either less than or equal to  b")
else:
   print ("Line 6 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 7 - b is either greater than  or equal to b")
else:
   print ("Line 7 - b is neither greater than  nor equal to b")

a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c += a
print ("Line 2 - Value of c is ", c)

c *= a
print ("Line 3 - Value of c is ", c)

c /= a
print ("Line 4 - Value of c is ", c)

c = 2
c %= a
print ("Line 5 - Value of c is ", c)

c **= a
print ("Line 6 - Value of c is ", c)

c //= a
print ("Line 7 - Value of c is ", c)

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100
print("Line 1 - Value of c is ", c)

c = a | b  # 61 = 0011 1101
print("Line 2 - Value of c is ", c)

c = a ^ b  # 49 = 0011 0001
print("Line 3 - Value of c is ", c)

c = ~a  # -61 = 1100 0011
print("Line 4 - Value of c is ", c)

c = a << 2  # 240 = 1111 0000
print("Line 5 - Value of c is ", c)

c = a >> 2  # 15 = 0000 1111
print("Line 6 - Value of c is ", c)

a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
    print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")

if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")

a = 2
if ( a in list ):
   print ("Line 3 - a is available in the given list")
else:
   print ("Line 3 - a is not available in the given list")


a = 20
b = 20

if ( a is b ):
   print ("Line 1 - a and b have same identity")
else:
   print ("Line 1 - a and b do not have same identity")

if ( id(a) == id(b) ):
    print ("Line 2 - a and b have same identity")
else:
   print ("Line 2 - a and b do not have same identity")

b = 30
if ( a is b ):
   print ("Line 3 - a and b have same identity")
else:
   print ("Line 3 - a and b do not have same identity")

if ( a is not b ):
   print ("Line 4 - a and b do not have same identity")
else:
   print ("Line 4 - a and b have same identity")


var = 100
if ( var == 100 ) :
    print ("Value of expression is 100")
print ("Good bye!")

var1 = 100
if var1:
   print ("1 - Got a true expression value")
   print (var1)

var2 = 1
if var2:
   print ("2 - Got a true expression value")
   print (var2)
print ("Good bye!")

var1 = 100
if var1:
   print ("1 - Got a true expression value")
   print (var1)
else:
   print ("1 - Got a false expression value")
   print (var1)

var2 = 0
if var2:
   print ("2 - Got a true expression value")
   print (var2)
else:
   print ("2 - Got a false expression value")
   print (var2)

print ("Good bye!")


var = 201
if var < 200:
   print ("Expression value is less than 200")
   if var == 150:
      print ("Which is 150")
   elif var == 100:
      print ("Which is 100")
   elif var == 50:
      print ("Which is 50")
   elif var < 50:
      print ("Expression value is less than 50")
else:
   print ("Could not find true expression")

print ("Good bye!")