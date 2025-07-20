## Day 1 - Python Introduction

Python language introduction
Python Syntax  Python Comments  Python 
Variables  Python Data Types  Python Numbers  Python Casting  Python 
Strings  Python Booleans  Python Operators  Python Lists  Python Tuples 
Python Sets  Python Dictionaries  Python If...Else  Python While Loops 
Python For Loops  Python Functions  Python Arrays User Input
Python Data Structures
OOP Basic Features
Python Classes and Objects
Python Inheritance
Python File Handling
List and Dictionary comprehentions
Custom List Implementation
Custom Dictionary Implementation
In terms of DS (Indexing, Order, Muteable, Duplicate)
Python builtin data types
Python user define data types

OOP Advance Features & Implementation
Python MRO (Method resolution order)
Python OOP Dimond problem
Python program execution mechanism (vs other langs)
Python Scope Local vs Global
Python Try Except
All false expressions in python
Python String Formatting (format method vs f object)
Dictionary built in methods
List built in methods
Python Dunders
Python Import sequence
OS module
sys module
Requests module
Datetime module
math module
json module
logging module
collections module
email module
re module
Python GIL
Threading module
Multiprocessing module
Python Decorators Feature (dafault and custom)
Python Closures Feature
Python Reduce Feature
Python Map Feature
Python Lambda/Anonynous Function
Python Generators (Generator vs Function)
Iterators
with statement
PEP8
PIP

---

## Interative Mode vs Scripted Mode

Interative mode is based on REPL and we execute the commands in interactive mode.

```shell
python
```

Scripted mode is the one we normally use as below. The interpreter take python code file as an input and execute it.

```shell
python filename.py
```

#### Using Shebang #!

at start of python file put this line to show which interepreter to use:

```python
#! /usr/bin/python3.11

print ("My first program")
price = 100
qty = 5
total = price*qty
print ("Total = ", total)
# chmod +x to make it executable
```

---

## IPython - Interactive python

it is enhanced version for interactive python and works as below:

```shell
ipython
```

it can be used to run magic commands like the following to run dir command:

```ipython
!dir *.exe
```

you can do *introspection* as follows:

```ipython
var = "Hello World"
var?
```

---

## Python Virtual Environment

![](/home/subhanali/.var/app/com.github.marktext.marktext/config/marktext/images/2025-06-19-15-29-46-image.png)

```shell
python -m venv myvenv
```

```shell
virtualenv --python=python3.12 myvenv
```

Common commands:

```shell
source myvenv/bin/activate
```

```shell
deactivate
```

```shell
pip freeze > requirements.txt
```

---

## Python Multi-Line Statements

```python
total = item_one + \
        item_two + \
        item_three
```

---

## Command Line Arguments

Many programs can be run to provide you with some basic information about how they should be run. Python enables you to do this with:

```shell
python -h
```

---

## Variables

Python's built-in **id()** function returns the address where the object is stored.

```ipython
Python 3.13.3 (main, Apr 22 2025, 00:00:00) [GCC 15.0.1 20250418 (Red Hat 15.0.1-0)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> "abc"
'abc'
>>> id("abc")
139968188171440
>>> 24
24
>>> id(24)
139968432332944
>>> id(34)
139968432333264
```

#### Deleting a variable / object

```python
del var
del var_a, var_b
```

Camel, Pascal, Snake case

```python
kmPerHour, KmPerHour, km_per_hour
```

#### Local vs Global variables

the main difference is the scope. Local is bounded with in the function and global variable is accessible throughout the program.

```python
x = 5
y = 10
def sum():
   sum = x + y
   return sum
print(sum())
```

here the **x** and **y** are global and accessible inside the **sum()**.

---

## Constants

doesn't have dedicated keyword for it. but we can use a convention:

```python
MY_CONST_VAR = 3.14
```

---

## C++ vs Python variables

in c++ each variable points to a unique memory location while in python if two variables have same value then they will point to the same **object**. But changes made to one will cause that variable to point to a **different object**.

#### C++

![named memory location](https://www.tutorialspoint.com/python/images/named_memory_location.jpg)

![Image-20](https://www.tutorialspoint.com/python/images/different_value_assigned.jpg)

#### Python

![address_100](https://www.tutorialspoint.com/python/images/address_100.jpg)

![address_150](https://www.tutorialspoint.com/python/images/address_150.jpg)

![address_200](https://www.tutorialspoint.com/python/images/address_200.jpg)

in above image, **garbage collector** will be envoked.

---

## Day 2 - Data Types and onwards

## Lists

```ipython
>>> l1 = [1, 2, 3]
>>> l1
[1, 2, 3]
>>> l2 = [4, 5, 6]
>>> l2
[4, 5, 6]
>>> l1 + l2 #concatination
[1, 2, 3, 4, 5, 6]
```

---

#### Byte Data Types

```python
# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)
```

```python
# Using prefix 'b' to create bytes
b2 = b'Hello'  
print(b2)
```

---

### Byte Array

```python
# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])  
print(value)  

# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')  
print(val)
```

---

#### Memory View

In Python, a memoryview is a built-in object that provides a view into 
the memory of the original object, generally objects that support the 
buffer protocol, such as byte arrays (bytearray) and bytes (bytes). It 
allows you to access the underlying data of the original object without 
copying it, providing efficient memory access for large datasets.

```python
data = b'Hello, world!'
# Creating a view of the last part of the data
view = memoryview(data[7:])  
print(view)
```

---

## Sequence Data Types

list, tuple, range

```python
#list
myList = [2023, "Python", 3.11, 5+6j, 1.23E-4]
#tuple
myTup = (2023, "Python", 3.11, 5+6j, 1.23E-4)
#range
range(start, stop, step)
```

bytes

```python
# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)

# Using prefix 'b' to create bytes
b2 = b'Hello'  
print(b2)
```

bytearrays

```python
# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])  
print(value)  

# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')  
print(val)
```

---

## Primitive vs Non primitive data types

primitive are Integers, Floats, Strings and Booleans.

non-primitve are Lists, Sets, Tuples, Dictionaries

#### Important Conversions:

| 1   | [Python int() function](https://www.tutorialspoint.com/python/python-int-function.htm) Converts x to an integer. base specifies the base if x is a string.                                            |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2   | [Python long() function](https://www.tutorialspoint.com/python/python-long-function.htm) Converts x to a long integer. base specifies the base if x is a string. *This function has been deprecated.* |
| 3   | [Python float() function](https://www.tutorialspoint.com/python/python-float-function.htm) Converts x to a floating-point number.                                                                     |
| 4   | [Python complex() function](https://www.tutorialspoint.com/python/python-complex-function.htm) Creates a complex number.                                                                              |
| 5   | [Python str() function](https://www.tutorialspoint.com/python/python-str-function.htm) Converts object x to a string representation.                                                                  |
| 6   | [Python repr() function](https://www.tutorialspoint.com/python/python-repr-function.htm) Converts object x to an expression string.                                                                   |
| 7   | [Python eval() function](https://www.tutorialspoint.com/python/python-eval-function.htm) Evaluates a string and returns an object.                                                                    |
| 8   | [Python tuple() function](https://www.tutorialspoint.com/python/python-tuple-function.htm) Converts s to a tuple.                                                                                     |
| 9   | [Python list() function](https://www.tutorialspoint.com/python/python-list-function.htm) Converts s to a list.                                                                                        |
| 10  | [Python set() function](https://www.tutorialspoint.com/python/python-set-function.htm) Converts s to a set.                                                                                           |
| 11  | [Python dict() function](https://www.tutorialspoint.com/python/python-dict-function.htm) Creates a dictionary. d must be a sequence of (key,value) tuples.                                            |
| 12  | [Python frozenset() function](https://www.tutorialspoint.com/python/python-frozenset-function.htm) Converts s to a frozen set.                                                                        |
| 13  | [Python chr() function](https://www.tutorialspoint.com/python/python-chr-function.htm) Converts an integer to a character.                                                                            |
| 14  | [Python unichr() function](https://www.tutorialspoint.com/python/python-unichr-function.htm) Converts an integer to a Unicode character.                                                              |
| 15  | [Python ord() function](https://www.tutorialspoint.com/python/python-ord-function.htm) Converts a single character to its integer value.                                                              |
| 16  | [Python hex() function](https://www.tutorialspoint.com/python/python-hex-function.htm) Converts an integer to a hexadecimal string.                                                                   |
| 17  | [Python oct() function](https://www.tutorialspoint.com/python/python-oct-function.htm) Converts an integer to an octal string.                                                                        |

---

## Type Casting

**Implicit Type Casting**: When programming lang decides itself

**Explicit**: When programmer specify the data type

🔧 **Python is dynamically typed** — object types are checked at runtime, not at compile time.

#### DownCasting

Parent class is converted into child class.

#### UpCasting

Child Class is treated as an instance of parent. We can't access child class methods and only accessible if we downcast it.

# Difference Between `set` and `frozenset` in Python

In Python, both `set` and `frozenset` are used to store **unordered collections of unique elements**, but they differ primarily in **mutability**.

---

## Comparison Table

| Feature        | `set`                          | `frozenset`                      |
| -------------- | ------------------------------ | -------------------------------- |
| **Mutability** | ✅ Mutable (can be changed)     | ❌ Immutable (cannot be changed)  |
| **Hashable**   | ❌ Not hashable                 | ✅ Hashable (can be dict/set key) |
| **Methods**    | Add/remove elements allowed    | No add/remove methods            |
| **Use case**   | Temporary, dynamic collections | Fixed sets, dictionary keys      |
| **Syntax**     | `set([1, 2, 3])`               | `frozenset([1, 2, 3])`           |

---

## Example: `set and frozenset`

```python
s = set([1, 2, 3])
s.add(4)
s.remove(2)
print(s)  # Output: {1, 3, 4}
```

```python
fs = frozenset([1, 2, 3])
# fs.add(4)  # ❌ Error: 'frozenset' object has no attribute 'add'
print(fs)   # Output: frozenset({1, 2, 3})
```

---

#### Unicode System - Encoding Decoding

```python
string = "Hello"
tobytes = string.encode('utf-8')
print (tobytes)
string = tobytes.decode('utf-8')
print (string)
```

#### Encoding

```python
s = "hello 😊"
b = s.encode('utf-8')
print(b)  # b'hello \xf0\x9f\x98\x8a'
```

#### Decoding

```python
text = b.decode('utf-8')
print(text)  # hello 😊
```

---

## OOP core principles

Encapsulation

Inheritance

Polymorphism

Abstraction

###### Encapsulation

Hiding data member and functions from other programmers or devlopers. Helps in storing sensitive data.

###### Inheritance

The relationship between base and derived class. The functions and data members of base class are available in derived.

###### Polymorphism

Poly means ***many***. When we implement the same function of base class inside the derived class then it shows the changed behaviour, this process is called polymorphism. Two types of polymorphism:

*runtime polymorphism*: the implementation in both methods is different.

*compile time polymorphism*: the datatypes of parameters is different.

###### Abstraction

Hiding the implementation details from **users** is called abstraction. This is used to improve the User Experience.

###### Parameters vs Arguments

| Feature    | Parameter             | Argument         |
| ---------- | --------------------- | ---------------- |
| Comes from | Function definition   | Function call    |
| Role       | Placeholder for input | Real input data  |
| Scope      | Local to function     | Passed by caller |

---


