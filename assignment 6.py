#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1. What are Escape characters? and how do you use them ?


Ans : Escape characters represent characters in string  values
    
    that would otherwise be difficult or impossible to type into code. 
    
    we can use the backslash character to escape a single character or symbol 
    
    example: \t, \n


# In[ ]:


Question 2. what do the escape character n and t stand for ?

Ans : \n is a newline, \t is a tab


# In[ ]:


Question 3. What is the way to include backslash character in a string.?

Ans: The \\ escape character will represent the backslash character in a string


# In[ ]:


Question 4 The string "Howl's Moving Castel" is a correct value.

why isn't the single quote character in the word Howl's not escaped a problem ?

Ans 4. The string "Howl's Moving Castle" escaped the problem because it is warpped

inside double quotes. if its wrapped inside single quotes then we have to use 

escape character \' to show single quote in the final output

'Howl\'s Moving castel' -> 'Howl's  Moving Castel'


# In[ ]:


get_ipython().set_next_input("Question 5. How do you write a string  of newline if you don't want to use the n character");get_ipython().run_line_magic('pinfo', 'character')

Ans: Multiline string allow you to use newlines in string without the \n escape character


# In[1]:


#example: 
a = '''iNeuron full stack 
Data Science Course'''
print(a)


# In[ ]:


get_ipython().set_next_input('Question 6. What are the values  of the given expresions');get_ipython().run_line_magic('pinfo', 'expresions')
   
       'Hello, world![1]'
       'Hello, World!'[0:5]
       'Hello , world!'[:5]
       'Hello,world!'[3:] 
    
    
Ans: The values for the given expression are:
        'Hello,world!'[1]-> 'e'
        'Hello,world!'[0:5]-> 'Hello'
        'Hello,world!'[:5] -> 'Hello'
        'Hello,world!'[:3] -> 'lo,world!'


# In[ ]:


get_ipython().set_next_input('Question 7. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')

'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()

Ans: The values for the given expressions are:
        
        'Hello'.upper() -> 'HELLO'
        'Hello'.upper().isupper()-> True
        'Hello'.upper().lower()-> 'hello'


# In[ ]:


get_ipython().set_next_input('Question 8. What are the values of the following expresions');get_ipython().run_line_magic('pinfo', 'expresions')

'Remember , remember,the fifth of july.'.split()-'join('There can only one'.split())'

Ans: The values for the given expression are: 'Remember,remember,the fifth of july.'.split() -> 
        ['Remember,','remember,','the','fifith','of','july.']
        '-'.join(There can only one'.split()) ->
                 'There-can-only-one'


# In[ ]:


Quetion 9. What are the methods for right-justifying,left-justifying
get_ipython().set_next_input('and centering a string');get_ipython().run_line_magic('pinfo', 'string')

Ans: The rjust(),ljust(),center()string methods, respectively


# In[ ]:


get_ipython().set_next_input('Question 10. What is the best way to remove whitespace character from the start or end');get_ipython().run_line_magic('pinfo', 'end')

Ans : The lstrip() and rstrip() methods remove whitespace characters from the left and right ends of a string respectively.

