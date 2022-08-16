#!/usr/bin/env python
# coding: utf-8

# Question 1.Create a zoo.py file first. Define the hours() function, which prints the string 
# 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.

# In[7]:


import zoo


# In[8]:


zoo.hours()


# Question 2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

# In[9]:


import zoo as menagerie


# In[11]:


menagerie.hours()


# Question 3. Using the interpreter, explicitly import and call the hours() function from zoo. 

# In[12]:


from zoo import hours
hours()


# Question 4. Import the hours() function as info and call it.

# In[13]:


from zoo import hours as info
info()


# Question 5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.

# In[14]:


plain_dict = {'a':1,'b':2,'c':3}
print(plain_dict)


# Question 6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?

# In[15]:


from collections import OrderedDict
fancy = OrderedDict(plain_dict)
print(f'plain_dict -> {plain_dict}')
print(f'fancy -> {fancy}')


# Question 7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].

# In[16]:


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])


# In[ ]:




