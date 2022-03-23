#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1.What are the two values of the Boolean data type? How do you write them?

#ans:  The two values of the Boolean data type is : True and False , and we have to use capital T and F and with the rest  of the word in lowercase.


# In[1]:


a = True
b = False
print(a,type(a))
print(b,type(b))


# # Question 2. What are the three different types of Boolean operators ?
# 
# #Ans:  There are three logical operators that are used to compare values. They  evaluate expressions down to Boolean values , returning either True or False. These operators are
#    #  and
#    #  or
#    # not

# In[6]:


a = 10
b = 20
print(a>5 and b>10) #example of boolean and
print(a>20 or b>10) #example of boolean or
print(not(a>1)) #example of boolean not


# In[ ]:


# Question 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate) ?
 
# ans : The Truth tables for the boolean tables are as follows:

* Truth Tables For and operator 
  
^ True and True is True 
^ True and False is False 
^ False and True is True 
^ False and False is False 

* Truth Table For or operator 

^ True and True is True 
^ True and False is True 
^ False and True is True 
^ False and False is False 

* Truth Table For not operator

^ True not is False False not is True


# In[ ]:


# Question 4. What are the values of the following expression ?
 
    * (5>4) and (3==5)
    * not (5>4)
    * (5>4) or (3==5)
    * not ((5>4) or (3==5))
    *(True and True) and (True == False)
    *(not False) or (not True)


# In[1]:


# Ans :

print((5>4) and (3==5)) #False
print(not(5>4)) # False
print((5>4) or (3==5)) # True
print(not((5>4) or (3==5))) # False
print((True and True) and(True==False)) # False
print((not False) or (not True)) # True


# In[ ]:


# Question 5. What are the six comparison operators ?

# Ans : The six comparision operators available in python are :
  == , != , < , > , <= , =>


# In[ ]:


# Question 6. How do you tell the difference between the equal to and assignment operators ? Decribe a condition and when you would use one ?

# Ans: IN python and many other programing language a single equal mark is used to assign a value to a varible, where as two consicutive equal marks is used to check whether 2 expressions give the same value.
 = is an assignment operator 
    
== is an equality operator    


# In[1]:


x = 10
y = 20
z = 20


# In[3]:


x==y

# is false because we assigned different values to x and y


# In[5]:


y==z

# is true because we assigend equal values to y and z


# In[ ]:


# Question 7. identify the three blocks in this code:

spam  = o
if spam ==10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')


# In[6]:


# Ans: in python, code block  referrs to a collection of code that is in the same block or indent. This is most commonly found in classes.functions and loops.

spam = 0
if spam ==10:
    print('eggs') #block #1
if spam  > 5 :
    print('bacon') #block #2
else:
    print('ham') #block #3
print('spam')
print('spam')


# In[ ]:


# Question 8. Write code that print Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam , and prints Greetings if anything else is stored in spam.


# In[7]:


#Ans:

def spamCode(spam):
    if spam==1:
        print('Hello')
    elif spam==2:
        print('Howdy')
    else:
        print('Greetings')
        
        
spamCode(1)
spamCode(2)
spamCode(3)        


# In[ ]:


# Question 9. if your programme is stuck in an endless loop , what keys you'll press?

#Ans : 'Ctrl-c' to stop a program stuck in an infinite loop


# In[ ]:


#  Question 10. How can you tell the difference between break and continue ?

#Ans : The 'break' statement will move the execution outside the loop if break condition is satisfied. Whereas the 'continue' statement will move the execution to the start of the loop.


# In[ ]:


# Question 11. in a for loop, what is the difference between range(10), range(0,10), and range(0,10,1)?

#Ans : The differences are as follows:

1. The range(10) call range from 0 to 9(but not inclued 10)
2. The range (0,10) explicitly tells the loop to start at 0
3. The range (0,10,1) explicitly tells the loop to increase the variable by 1 on each iteration


# In[ ]:


# Question 12. Write a short program that prints the numbers 1  to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop ?


# In[8]:


# Ans:  

print('-'*10 , 'Using For Loop','-'*10)
for i in range(1,11):
    print(i, end =" ")
print('\n')
print('-'*10, 'using While Loop', '-'*10)
i=1
while i<=10:
    print(i,end="")
    i+=1


# In[ ]:


# Question 13. if you had a function named bacon() inside a module named spam , how would you call it after  importing spam ?

# Ans : This function can be called with  'spam.bacon()'.

