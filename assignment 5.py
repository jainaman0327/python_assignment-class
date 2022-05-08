#!/usr/bin/env python
# coding: utf-8

# In[2]:


##Question 1. What does an empty dictionary's code look like?


#Ans: An empty dictionary is often represented by two empty curly brackets


 #   d = {}  or d = dict()


# In[3]:


# Question 2. What is the value of dictionary value with key 'foo' and the value 42 ?

# Ans : {'foo':42}


# In[4]:


# Question 3. What is the most significant distinction between a dictionary and a list?

# Ans : Dictionaries are represented by {} where as listed are represented by [] .

#The items stored in a dictionary are unordered, while the items in a list are orderd 


# In[5]:


# Question 4. What happens if you try to access spam['foo'] if spam is {'bar':100}?

spam = {'bar':100}
spam['foo']


# In[ ]:


we will get a keyError __KeyError :'foo'


# In[ ]:


#Question 5. if a dictionary is stored in spam, what is the difference between the expression 'cat' in spam and 'cat' in spam.keys()?

#Ans: There is no difference. The operator checks whether a value exits as a key in the dictionary or not


# In[6]:


# Question 6. if a dictionary is stored in spam, what is the differernce between the expression 'cat' in spam and 'cat' in spam.values()?

#Ans : 'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.vlaues() checks whether there is a value 'cat' for one of the keys in spam.


# In[7]:


# Question 7. What is a shortcut for the following code?

if 'color' not in spam:
    spam['color'] = 'black'


# In[8]:


#Ans: spam.setdefault('color','black')


# In[9]:


# Question 8. How do you 'pretty print' dictionary values using which modules and function ?

#Ans: we can pretty print a dictionary using three functions

1. by using pprint() function of pprint module 

* Note: pprint() function doesnot prettiy nested dictionaries 
    
2. by using dumps() method of json module
3. by using dumps() method of yaml module


# In[1]:


ndict = [ 
    {'Name': 'john', 'Age':'23','Residence':{'country':'USA','city':'New York'}},
    {'Name':'Ram','Age':'44','Residence':{'country':'india','city':'Bhopal'}},
    {'Name':'lee','Age':'29','Residence':{'country':'japan','city':'Hirosima'}},
    {'Name':'Anne','Age':'35','Residence':{'country':'uk','city':'England'}}
    
]

print('printing using print() function\n',ndict)
print('-'*70)
import pprint
print('printing using pprint() function')
pprint.pprint(ndict)
print('-'*70)
import json
dump = json.dumps(ndict, indent = 4)
print('-'*70)
import yaml
dump = yaml.dump(ndict)
print('printing using dump() method\n', dump)


# In[ ]:




