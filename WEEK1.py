#DATA TYPES
# It is a phenomenon of classifying the types of data .

# Every data has a unique structure at the same time functonslity type.mro

# Data types has classified into 2 types :
# 1) primitive data types
# 2)non-priitive data types

# Data types are contains in the two ways:
# 1)mutable data types
# 2)Immutable data types

# 1)Mutable data types:

# A data type who's original value can be changed is called Mutable data types.

# ex:list
l=["ashok","venky","ram"]
var.append(ele)
l.append("rathod")
l

# 2)Immutable data types:

# A data types who's orignal value cannot be changed is called Immutable data types.

# EX:str

# S="koy koy"
# S.upper()
# #'koy koy'
# -------------------------------------------------------------------------------------

# !) Primitive data types:

# 1.it is a single value data type
# 2.it is stored in single block of memory.
# 3.Immutable data types.
# 4.Is has a fixed length of Memory.

# Primitive data types are classified into 3 types:

# 1.Numeric type------>(Int,float,Complex)
# 2.boolean type----->(True , False)
# 3.None type(None)

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# 1.Numeric type------>(Int,float,Complex)

# !)Integer:
# It is represented as postive infinte to negitive infinite without decimal points.

# it is a fixed length of memory 

# it is contains -5 to 256 numbers are considered as 32 bit memory , so it obeys memory reusability.

# it has a single value data types and Immutable data types.AsyncGeneratorType

# Real number without decimal point.

# Default value is '0' and Int().
# -------------------------------------------------------------------------------
# Ways to creating Int Data type:

# !)direct assgining:

n=33
n
# ---->33

# 2)By using Built in data types:

n1=int(24)
n1
# ----> 24

# 3) Default Value 

n2= int()
n2
# ---->0
-------------------------------------------------------------------------------------
# 2) float  data types:

# Single value dta type

# Immutable data type

# represented as real with decimal point.

# default value is 0.0 and float()

# it can be positive and negitive.

# it will take 64 bit memory.

# Ways to creating Float Data type:
# -------------------------------------------------------------------------------------
# !)direct assigning :

f=1.3
f
# --->1.3

# 2) class object:

f1=float(23.3)
f1
# --->23.3

# 3) Default Value
f2=float()
f2
# ---->0.0

# 3) complex data type:
# -----------------------------------------------------------------------------------
# Single value, Immutable data type
# Represented as real numbers and imiginary numbers.

# SYNTAX: V_name= a+bj

# it can be both (+ and -) numbers.

# Default value is 0j.

# it will take 64 bit memory.

# Ways to creating complex Data type:
# -------------------------------------------------------------------------------------
# !)direct assigning :

a=9+3j
a
# ---->(9+2j)
# 2) class object:

a=complex(9,2)
# ----->9+2j

a=complex(9)
# -----> 9+0j

a=complex(2j)
# -----> 2j

a=complex(9+2j)
# ----> 9+2j

# 3) Default Value
a=complex()
a
# ------>0j

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
# 2)BOOLEAN DATA TYPES:

# It is immutable data type.
# Represented as True or False.
# In programming lnguage true---->1 and False---->0.
# Used for checking hweather the condition satisfied or not.

# true---->1
# False---->0
# Defaulte valueis ---->False

# consider 32 bit memory.

# Ways to creating complex Data type:
# ------------------------------------------------------------------------------------
# !)direct assigning :
# t=True
# f=False

# 2) class object:

t1=bool(1)
t1
# ------>True 

f1=bool(0)
f1
# ----->False

# 3) Default value:

f2=bool()
f2
# ----->False

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

# NONE DATA TYPE:-

# none type means null,nothing,empty

# Single value data type

# In memory block , Interpreter will store ASCII value of none()

# When we dont know that type of value to be stored then we use none.

# Nothing can be performed.

# 32 bit memory it contains.

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

2) NON-PRIMITIVE DATA TYPES:

Multi value data type.

all multiple values are stored in the multiple blocks of memory.

Combination of mutable  and immutable data types.

variable lenght of memory.

Each non-primitive block has uniquie address.

Each and every sub block has their sub address.
----------------------------------------------------------------------------------------------------------------------
!) STRING DATA TYPE:
 IT IS a collection of characters .

it can have lower case , upper case , number, special character,spaces.

Boundary comditions are-----> "  "

It can have duplicate charaters.

it is immutable data type .

it will take both 32 and 64 bit memory.

lenght of string -----> len(String) 

# Ways to creating string Data type:
---------------------------------------------------------------------------------------
# Direct assign:

by single quotes (' ')----->'hello'

by double qoutes(" ")------->"ashok"

by single triple qoutes('''  ''')----->'''ashok venkat'''

lenght of the string (""" rambabu""")

2)class object :

S=str('ashok')

S ----->'ashok'

3) Default value:

S=str()
s ----->' '

ex:-

S="ashok venkat"
len(S)
S[0]
S[4]
S[7]
------------------------------------------------------------------------------------------
2) LIST DATA TYPES:-

List is a collection of datatypes.

list is a collection of Homogenous and heterogeneous type elements seperated by comaa.

list can have duplicates.

elements in the list are ordered.

Boundary Conditions are :----->[]

# Ways to creating list Data type:
----------------------------------------------------------------------------------------
1)Direct assign:
l=[1,2,3,4]
2)class object:
l=list([1,1.2,12])
3)default value:
l=list[]
l------> []

ex:
l=[11,22.3,'hello',[12,2+3j,True]]
l[2]
l[3]
l[0]
l[2][1]
l[-2]
l[2][-2]
l[2][0]
---------------------------------------------------------------------------------
3) TUPLE DATA TYPE:

It is a collection of homogenous and heterogenous elements.

data is separated by comma.

Boundary condtions: ----> ()

it can have duplicate values.

it is a ordred .

it is a immutable data type.

it will take 64 bit memory.

indexing and slicing is done in tuple.

# Ways to creating tuple Data type:
!) Direct assign 

t=(1,2,3)

2) class object
t=tuple((1,2,3))

3)Default value:
t=tuple()
t----->()

ex:-
t=(11,"hello",2,[111,23.3])
t[0]
t[3]
t[-3]

3) SET DATA TYPE:

----------------------------------------------------------------------------------------------------
# Input and Output in Python:

# Understanding input and output operations is fundamental to Python programming. With the print() function,
# we can display output in various formats, while the input() function enables interaction with users by gathering input during program execution.

# Taking input in Python:

# Python's input() function is used to take user input. By default, it returns the user input in form of a string. 

# Example:

name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

# Output

# Enter your name: GeeksforGeeks
# Hello, GeeksforGeeks ! Welcome!

# Printing Output using print():

# At its core, printing output in Python is straightforward, thanks to the print() function.
# This function allows us to display text, variables and expressions on the console. Let's begin with the basic usage of the print() function:

# In this example, "Hello, World!" is a string literal enclosed within double quotes. When executed, this statement will output the text to the console.


print("Hello, World!")

# Output
# Hello, World!

Print Numbers in Python:

# The code prompts the user to input an integer representing the number of roses,
# converts the input to an integer using typecasting and then prints the integer value.


# Taking input as int
# Typecasting to int
n = int(input("How many roses?: "))
print(n)

# Output

# How many roses?: 88
# 88
-------------------------------------------------------------------------------------------
Python Operators:


# In Python programming, Operators in general are used to perform operations on values and variables.

# Operators: Special symbols like -, + , * , /, etc.
# Operands: Value on which the operator is applied.

# Types of Operators in Python
# Operators-in-python

# Arithmetic Operators
# Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.



# Variables
a = 15
b = 4
​
# Addition
print("Addition:", a + b)  
​
# Subtraction
print("Subtraction:", a - b) 
​
# Multiplication
print("Multiplication:", a * b)  
​
# Division
print("Division:", a / b) 
​
# Floor Division
print("Floor Division:", a // b)  
​
# Modulus
print("Modulus:", a % b) 
​
# Exponentiation
print("Exponentiation:", a ** b)

# Output
# Addition: 19
# Subtraction: 11
# Multiplication: 60
# Division: 3.75
# Floor Division: 3
# Modulus: 3
# Exponentiation: 50625
# Note: Refer to Differences between / and //.
----------------------------------------------------------------------------------------------------------------------

# Comparison Operators:

# In Python, Comparison (or Relational) operators compares values. It either returns True or False according to the condition.

a = 13
b = 33
​
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Output
# False
# True
# False
# True
# False
# True
------------------------------------------------------------------------------------------------------
# Logical Operators:

# Python Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

# The precedence of Logical Operators in Python is as follows:

Logical not
logical and
logical or

a = True
b = False
print(a and b)
print(a or b)
print(not a)

# Output
# False
# True
# False
------------------------------------------------------------------------------------------------------------------
# Bitwise Operators:
# Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

# Bitwise Operators in Python are as follows:

# Bitwise NOT
# Bitwise Shift
# Bitwise AND
# Bitwise XOR
# Bitwise OR

a = 10
b = 4
​
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# Output
# 0
# 14
# -11
# 14
# 2
# 40
----------------------------------------------------------------------------------------------
# Assignment Operators:
# Python Assignment operators are used to assign values to the variables. 
# This operator is used to assign the value of the right side of the expression to the left side operand.

# Example
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

# Output
# 10
# 20
# 10
# 100
# 102400
-----------------------------------------------------------------------------------------------------
# Identity Operators:

# In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

# is------->True if the operands are identical 
# is not------->True if the operands are not identical 

a = 10
b = 20
c = a
​
print(a is not b)
print(a is c)

# Output
# True
# True
------------------------------------------------------------------------------------------------------
# Membership Operators:

# In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.

# in ------->True if value is found in the sequence
# not in ------------> True if value is not found in the sequence

x = 24
y = 20
list = [10, 20, 30, 40, 50]
​
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
​
if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

# Output
# x is NOT present in given list
# y is present in given list

--------------------------------------------------------------------------------------------------------
# Ternary Operator:

# in Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. 

# It simply allows testing a condition in a single line replacing the multiline if-else, making the code compact.

# Syntax :  [on_true] if [expression] else [on_false] 


a, b = 10, 20
min = a if a < b else b
​
print(min)

# Output
# 10
---------------------------------------------------------------------------------------------
# Precedence and Associativity of Operators:

# In Python, Operator precedence and associativity determine the priorities of the operator.

# Operator Precedence:
# This is used in an expression with more than one operator with different precedence to determine which operation to perform first.




expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0
​
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

# Output
# 610
# Hello! Welcome.

# Operator Associativity:

# If an expression contains two or more operators with the same precedence then Operator Associativity is used to determine.
#  It can either be Left to Right or from Right to Left.

print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)

# Output
# 100.0
# 6
# 0
# 512





# CONDTIONAL STATEMENTS:

# * TO APPLY THE CONDITIONS WE WILL USE CONDITIONAL STATEMENTS.
# * THE SET OF STATEMENTS WILL EXCUTE BASED ON THE DECISION ONLY ONE TIME.

# THE ARE CLASSIFIED INTO 5 TYPES:
#     1.IF STATEMENT
#     2.ELSE STATEMENT
#     3.ELIF STATEMENT
#     4.NESTED IF STATEMENT
#     5.MATCH CASE

# 1.SIMPLE IF STATEMENT:
#     IF KEYWORD WILL CHECK THE FINAL RESULT IS TRU/FALSE.
#     IF IT IS TRUE IT EXCUTES TRUE BLOCK TSTEMENT,OTHERWISE IT WILL SEND THE CONTROLLER TO EITHER ELSE OR ELIF OR OUT OF THE ENTIRE BLOCK.

# SYNTAX: IF CONDITION / EXPRESSION :

#     (TRUE BLOCK STATEMENT )
#     ELSE:
#     (FLASE BLOCK STATEMENT)

# ELIF STATEMENT:

# IN THIS STATEMENT WE CAN WRITE ONE OR MORE THAN ONE CONDITION.

# ONE IF STATEMENT SHOULD BE PRESENT.

# ELIF, WE CAN WRITE 'N' NO.OF ELIF STATEMENTS BASED ON SITUATION.

# ELSE STATEMENT IS OPTIONAL.

# SYNTAX:
# IF CONDITION:
#      (TBS)
# ELIF CONDITION:
#      (TBS)
# ELSE(OPTIONAL):
#     (FBS)

# Q1) WAP TO CHECK THE NUMBER IS EVEN AND POSITIVE?

n=int(input("enter a number :"))
if n % 2== 0 and n>0:
    print("it is positive and even")
else:
    print("it is not positive or not even ")

# Q2) WAP TO CHECK THE NUMBER IS ODD AND NEGITIVE?

n=int(input("enter a number :"))
if n % 2!= 0 and n<0:
    print("it is negitive and odd")
else:
     print("it is not negitive or not odd ")

# Q3)WAP TO CHECK THE NUMBER IS POSITIVE OR NOT IF IT IS POSITIVE SQUARE THAT THE NUMBER ELSE CUBE THE NUMBER ?

n=int(input("enter a number:"))
if n%2==0:
    print(F" the given number is {n} and square of that number is : {n**2}")
else:
    print(F" the given number is {n} and cube of that number is : {n**3}")

# LOOPING STATEMENTS

# DEF:  looping statements are used to sxcute a block of code repeatdly.

# types:

# 1.WHIE LOOP
# 2.FOR LOOP.

# ABOUT THE BOTH LOOPS:

# FOR LOOP:
# iterate over asequence(e.g,list,set,tuple)on other iterable object.

# WHILE LOOP:
# repeat a block of code as long as a specefied condtion is true.

# WHILE LOOP SYNTAX:

# initilization

#     while condition:

#     updation(increament/decreament)

# FOR LOOP SYNTAX:

#     for ref_var in cellection:

#     for ref_var in built in methods:


# WHEN WE USE THE "WHILE" LOOP:

# when we doon't know the how many time

# Q1) WAP TO PRINT THE 1 TO 10 NUMBERS?
start =1
end=10

while start <= end:
    print(start)

    start +=1

# Q2) WAP TO PRINT THE 5 TO 1 NUMBERS?
start =5
end=1

while start >= end:
    print(start)

    start -=1

# FOR LOOP

# It is used to when the number of iterations to be done is known.

# there is no need to keep the iteration as for loop do it implicitly.

# no need to increament the referenc3e variable manually.

# sytanx:

# for ref_var in collection:

# for ref_var in built in methods:

# Q1) WAP TO ITERATE OVER ASTRING AND PRINT THE CHARACTER AT A TIME?

s="hello"

for char in s:
    print(char)

# Q2) WAP TO ITERATE OVER A LIST  AND PRINT THE ELEMNT AT A TIME?
s=[1,"hi",1.2]

for ele in s:
    print(ele)
