#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1. What exectly is [ ] ?

# Ans: The empty list represented by [ ] is a list that contains no items. This is similar to  '' which represents an empty string.


# In[3]:


# Question 2. In a list o values stored in a variable called spam, how would you assing the value 'hello' as the third value ? (Assume [2,4,6,8,10] are in spam.)

# Ans: spam[2] = 'hello' (Note : Lists follows zero based indexing) 

#example 
spam = [2,4,6,8,10]
print(spam)
spam[2]  = 'hello' #list uses zero based indexing
print(spam)


# # Let's pretend the spam includes the list  ['a', 'b' , 'c', 'd'] for the next three queries.

# In[4]:


# Question 3. What is the value of spam[int(int('3'*2)//11)] ?

# Ans: 'd' (Note  that '3'*2 is the string '33' which is passed to int() before being divied by 11. This eveluates to 3, spam[3] is equal to d.)


spam = ['a','b','c','d']
print("spam[int(int('3'*2)//11)] ->", spam[int(int('3'*2)//11)])


# In[2]:


# Question 4. What is the value of spam[-1]?

# Ans: 'd' (Lists support Negative indexing , Hence spam[-1] returns 'd')


spam = ['a','b','c','d']
print('spam[-1]->)' , spam[-1])


# In[3]:


# Question 5. What is the vlaue of spam[:2]?

#Ans : spam[:2] returns all elements in the list spam from 0 to 2 exclding 2

print(spam)
print(spam[:2])


# # Let's pretend bacon has the list [3.14, 'cat',11, 'cat' True]  for the next three question
# 

# In[4]:


# Question. 6  What is the value of bacon.index('cat')?

# Ans: The value of bacon.index('cat') is 1 (Note: index method returns the index of first occuerrnce of 'cat')



bacon = [3.14, 'cat' , 11, 'cat', True]
print("bacon.index('cat')->",bacon.index('cat'))


# In[5]:


#Question 7. How does bacon.append(99) change the look of the list value in bacon.?

#Ans: The append method adds new element to the end of the list


#Example 
print(bacon)
bacon.append(99) #append 99 to the end of the list 
print(bacon)


# In[6]:


# Question 8. How does bacon.remove('cat') change the look of the list in bacon?

# Ans: The remove method removes the first occurence of the element in the list

print(bacon)
bacon.remove('cat')
print(bacon)


# In[7]:


#Question 9. What are the list concatenation and list replication operation ?

#Ans: The operator for list concatenation is + , while the operator for replication is *.(This is the ssame as for strings.)

#Example 
list_1 = ['ML','DL','AI','CV','NLP']
list_2 = ['RNN', 'CNN','SVN']
print(list_1+ list_2) #list concatenaton
print(list_2*2) # List Replication


# In[8]:


#Question 10. What is the difference between the list method append() and insert()?

#Ans: While append() will add values only to the end of a list , insert() can add them anywhere in the list.

#Examples 
list = [1,2,3,4,5]
list.append(6)
print(list)
list.insert(2,'Demo')
print(list)


# In[1]:


# Question 11. What are the two method for removing items from list?

#Ans: The 'del' statement and the 'remove()' method are two ways to remove values from a list.


# In[2]:


#Question 12. Describe how list values and string values are identical.

#Ans: Both lists and strings can be passed to 'len()' function, have indexes and slices, be used  in 'for' loops, be concatenated or replicated, and be used with the 'in' and 'not in' operators.


# In[3]:


#Question 13. What's the differance between tuples and lists?

#Ans: Lists are Mutable , Indexable and Slicable. they can have values added, removed, or changed. Tuples are Immutable but Indexable and Slicable. the tuple values cannot be  changed at all.Also,tuples are represented using parentheses,'()' ,while lists use the square brackets,'[]'.


# In[4]:


# Question 14. How do you type a tuple value that only contains the integer 42?

#Ans : (42) (The trailing comma is mandatory. otherwise its considered as a int by python interpreter)


tup1 = (42)
tup2 = (42)
print(type(tup1))
print(type(tup2))


# In[6]:


# Question 15. How do you get a list values tuple from? How do you get a tuple values list form?

# Ans: ## list into a tuple

#Approach 1 : Using Tuple(list_name).

#Typecasting to tuple can be done by simply using tuple(list_name).

def convert(list):
    return tuple(list)

# Driver function 
list = [1,2,3,4]
print(convert(list))


# In[7]:


# Approach 2.
# A small variation to the above approach is to use a loop inside tuple().

def convert(list):
    return tuple(i  for i in list)

# Driver function
list = [1,2,3,4]
print(convert(list))


# In[2]:


# convert Tuple into List

# To convert a tuple into list in python, call list() builtin function and pass the tuple as argument to the function. list() return a new list generated from the items of the given tuple.


# initialize tuple 
aTuple = (True, 28 , 'Tiger')

# tuple to  list 
aList = list(aTuple)

#print list
print(type(aList))
print(aList)


# In[3]:


# Question 16. Variable that "contain" list values are not necessarily lists themselves. insted, what do they contain?

# Ans: They contain references to list values.


# In[4]:


# Question 17. How do you distinguish between copy.copy() and copy.deepcopy()?


#Ans : The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is , only copy.deepcopy() wil duplicate any lists inside the list.


# In[ ]:




