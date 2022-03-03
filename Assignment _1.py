#!/usr/bin/env python
# coding: utf-8

# question no.1 :- In the below element which of them are values or an expressin ? 
#     
#     *
#     'hello'
#     -87.8
#     -
#     /
#     +
#     6
# 

# # ##Ans of Question no.1
#     
#    # values (integer):- (-87.8),(6)
#    
#    # values(string):- ('hello')
#    
#    # expression(mathamtical operators) :-(*) , (-) ,(/) ,(+)    

# # question no 2 :- what is the diffrence between string and variable ?
# 
# ## answer: in python , string is an immutable sequance data type. it is the sequance of unicode characters wrapped inside single , double  , or triple quotes.
# 
#     example: 1. 'this is a single quotes string in python'
#     
#             2. "this is a double quotes string in python"
#             
#             3.'''this is a triple quotes string in python'''
#             
#            4. """this is a triple double string in python"""
#       
#  ## variable: A python variable is a reserved memory location to store values. in other words, a   python program gives data to the computer for processing, every value in python has a datatype. Deffrent data type in python are Numbers, List , Tuple, Strings, Dectionary, etc. Variable can be declared by any name or even alphabets like  a , aa , abc , etc
#  
#  ## in python you cannot concatenate string  with number directly, you need to declare them as a separate variable , and after that , you can concatenate number with string.        

# # Question no. 3 :- Describe three different data types.
# 
# answer:- Data type are the classification of data items. it represents the kind of value that tells what operation can be performed on a particuler data. Since everything is an object in Python programming, data types are actually classes and variable are object of these classes.
#     
#     following are the standard or built in data type of python:
#         
#         1. Numeric 
#         2. Sequence 
#         3. Boolean
#         4. Set
#         5. Dictionary
#         
#         
#              ## Numeric ##
#              
#       In python, numeric data type represent the data which has numeric value. Numeric value can be integer , floating number or even complex numbers.
#       
#       # Integer :-  this vlaue is represented by int class. it contains positive or negitive whole numbers(whitout fraction or decimal). in python there is no limit to how long an integer vlaue can be.
#       
#   # Float :- this value is represented by float class. it is a real number with floating point representation. it is specified by a decimal point. optionally, the character e or E followed by a positive  or negative integer may be appended to specify scientific notation.
#   
#  # Complex Numbers :- complex number is represented by complex class. it is specified as (real part) + (imaginary part)j. for example:  5 + 8j
#  
#  

# In[10]:


# python program to 
# demonstrate numeric value

a = 9
print("\nType of a:" , type(a))

b = 6.6
print("\nType of b:", type(b))

c = 5+ 8j
print("\nType of c:", type(c))


# #             ## Sequance Type ##     
#              
#  In python , sequance is the ordered collection of similar or different data types. Sequance allows to store multiple vlaues in an organized and efficient fashion. There are several squance types in python - 
#  
#  # String 
#  # List
#  # Tuple
#  
#  1.) String :- In python , strings are arrays of bytes represting unicode characters . A string is a collection of one more characters put in a single quote , double - quote or triple quote. In python there is no character data type , a character is a string of lenth one. it is represented by -- str Class.

# In[4]:


# creating string 
# creating a string with single Quotes 

Strings1 = 'Full stack data scince assignment 1 '
print('string with the use of single Quotes: ')
print(Strings1)
print(type(Strings1))

# creating a string with double Quotes

Strings2 = "hello my name is aman"
print("\nString with the use of double Quotes:")
print(Strings2)
print(type(Strings2))

# creating a string with triple Quotes

Strings3 = '''i am from madhya pradesh'''
print('''\nString with the use of Triple Quotes:''')
print(Strings3)
print(type(Strings3))

# creating String with triple Quotes allows multiple lines

String4 = '''\nTarak mehta
                  ka
                ooltha chashmah'''

print('''\ncreating a multiline string :''')
print(String4)


# # Accessing elements of String
# 
# In Python , individual characters of a String can be accessed by using the method of indexing allows negative address references to access character, -2 refers to the second last character and so on.

# In[4]:


# python program to Access characters of string

String1 = "jay hind jay bharat"
print("\nInitial string:")
print(String1)

# printing First character 
print("\nFirst character of string is:")
print(String1[0])

# printing Last character
print("\nlast character of String is:")
print(String1[-1])


# # 2) List
# 
#  Lists are just like the arrays , declared in other languages which is a ordered collection of data.
#  it is very flexible as the items in a list do not need to be of the same type.
# 
# 

# In[7]:


#Creating List

#Lists in python can be created by just placing the sequence inside the square brackets[].

# python program to demonstrate creating of list

#creating a list
list = []
print("\nblank list")
print(list)

# creating a list with the use of a String
list = ['mera bharat mahan']
print("\nList with the use of string:")
print(list)

# Creating a list with the use of multiple values
list = ["hello", "hii","how are you"]
print("\nList containting multiple values:")
print(list[0])
print(list[2])

# Creating a multi - Dimensional List (by Nesting a list inside a List)
list = [['ram','shyaam'],['geeta']]
print("\nMulti-Dimensional list:")
print(list)


# # Accessing elements of List 
# 
# In order to access the iist items refer to the index number.
# Use the index operater [] to access an item in a list. 
# In python, negative sequence indexes represent positions from the end of the array.
# instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3].
# Negative indexing means beginnig from the end , -1 refers to the last item , -2 refers to the second - last item , etc.

# In[6]:


# python program to demonstrate accessing  of element from list

# Creating a list with the use of multiple values

list = ["my","your","other"]
    
#  accessing a element from the list using index number
print("\nAccessing element from the list")
print(list[0])
print(list[2])

# accessing a element using negative indexing 
print("\nAccessing element using negative indexing")

# print the last element of list
print(list[-1])

# print the third last element of list
print(list[-3])


# # 3). Tuple
# 
# Just like list ,tuple is also an ordered collection of python objects.
# The only difference between tuple and list is that tuples are immutable i.e. tuples cannot be modified after it is created.
# it is represented by tuple Class.
# 
# Creating Tuple
# In, python ,tuples are created by placing a sequence of values separated by 'comma' with or without the use of parentheses for grouping of the data sequence.
# Tuples can contain any number of elements and of any datatype (like string , integer ,list, etc.).

# In[4]:


# python program to demonstrate creating of set

# creating an empty tuple
Tuple1 = ()
print("initial empty Tuple:")
print(Tuple1)

# creating a Tuple with the use of strings

Tuple1 = ('hello', 'you')
print("\n|Tuple with the use of String:")
print(Tuple1)

# Crreating a Tuple with the use of built - in function

Tuple1 = tuple('hello')
print("\nTuple with the use of function :")
print(Tuple1)

# Creating a Tuple with nested tuples

Tuple1 = (0,1,2,3)
Tuple2 = ("pyton", ("language"))
Tuple3 = (Tuple1 , Tuple2)
print("\nTuple with nested tuples:")
print(Tuple3)


# # Accessing element of Tuple 
# 
# in order to access the tuple items refer to the index number. 
# use the index operator[ ] to access an item in tuple. 
# The index must be an integer. Nested tuples are accessed using nested indexing.

# In[5]:


# Python program to demonstrate accessing tuple 

tuple1 = tuple([1,2,3,4,5,6])

# Accessing element using indexing 
print("frist element of tuple")
print(tuple1[0])

# Accessing element from last negative indexing 
print("\nLast element of tuple")
print("tuple[-1]")

print("\nThird last element of tuple")
print(tuple1[-3])


#                                  ## Boolean ##
#     
#     Data type with one of the two built - in values, True or False.
#     Boolean objects that are equal to True are turthy(true), and 
#     those equal to False are falsy(false). But non-Boolean objects 
#     can be evaluated in Boolean Context as well and determind to be true 
#     or false. It is denoted by the Class bool.
#     

# In[7]:


# Python program to demonstrate boolean type

print(type(True))
print(type(False))


# # Question 4. What is an expression made up of? What do all expressions do?
# 
# ## Ans:-  An expression is a combination of operator and operands that is interpreted to produce some other value. In any programing language, an expression is evaluated as per the precedence of its operators.  If you ask python to print an expressions , the interpreter evaluates the expression and displays the result.
# 

# # Question 5.  . This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 
# ## Ans :- Expression is made up of values, containers,  and mathematical operators and the statement is just like a command that a python interpreter executes like print.
# 

# # Question 6. After running the following code, what  does the variable bacon contain?
# bacon = 22
# 
# bacon = +1
# 
# ## Ans :-  it gives 23 as execution code
# 

# In[4]:


bacon = 22


# In[5]:


bacon +1


# #  Question 7. what should the values of the following two terms be.?
# 
#  'spam' + 'spamspam'
#  
#  'spam'* 3
#  
#  ## Ans :- it will be the same

# In[6]:


'spam' + 'spamspam'


# In[7]:


'spam'* 3


# # Question 8. Why is eggs a valid variable name while 100 is invalid.?
# 
# ## Ans :- because we can't start giving variable an integer name. if we , we should begin with , a string - like alphabet name then integer . e100 or eggs100 is valid.

# # Question 9. What three function can be used to get the integer , floating - point number , or string version of a value.?
# 
# ## Ans :- str() ,int() , float()

# # Question 10. why does this expression cause an error?  How can you fix it?
#  
#  'I have eaten' + 99 + 'burritos'
# 
# ## Ans :- because 99 is an integer it cannot be concatenated with strings, if we have to concatenate it we need to do typecasting.
#  
