#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1. Create a list called years_list,
starting with the year of your birth, and each
year thereafter until the year of your fifth birthday.
For example, if you were born in 1980. the list would be 
years_list = [1980, 1981, 1982, 1983, 1984, 1985].


# In[1]:


years_list = [ele for ele in range(1997,1997+6)]
print(years_list)


# In[ ]:


Question 2. In which year in years_list was your third birthday? 
Remember, you were 0 years of age for your first year.


# In[2]:



print(years_list[3])


# In[ ]:


get_ipython().set_next_input('Question 3.In the years list, which year were you the oldest');get_ipython().run_line_magic('pinfo', 'oldest')


# In[3]:


print(years_list[-1])


# In[ ]:


Question  4. Make a list called things with these three strings 
as elements: "mozzarella", "cinderella", "salmonella".


# In[4]:


things = [ele+'ella' for ele in ['mozzar','cinder','salmon']]
print(things)


# In[ ]:


Question 5. Capitalize the element in things
that refers to a person and then print the list. 
get_ipython().set_next_input('Did it change the element in the list');get_ipython().run_line_magic('pinfo', 'list')


# In[5]:


for ele in range(len(things)):
    if things[ele] == 'cinderella':
        things[ele] = things[ele].capitalize()
print(things)


# In[ ]:


Question 6. Make a surprise list with the elements "Groucho," "Chico,"
and "Harpo."


# In[6]:


suprise_list = ['Groucho','Chico','Harpo']
print(suprise_list)


# In[ ]:


Question 7. Lowercase the last element of the surprise list,
reverse it, and then capitalize it.


# In[7]:


print(suprise_list[-1].lower()[::-1].capitalize())


# In[ ]:


Question 8. Make an English-to-French dictionary called e2f and print it. 
Here are your starter words: dog is chien, cat is chat, and walrus is morse.


# In[8]:


e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)


# In[ ]:


Question 9. Write the French word for walrus in your three-word dictionary e2f.


# In[9]:


print(e2f.get('walrus'))


# In[ ]:


Question 10. Make a French-to-English dictionary called f2e from e2f.
Use the items method.


# In[10]:


f2e = dict([ele[::-1] for ele in e2f.items()])
print(f2e)


# In[ ]:


Question 11. Print the English version of the French word
chien using f2e.


# In[11]:


print(f2e.get('chien'))


# In[ ]:


Question 12. Make and print a set of English words from 
the keys in e2f.


# In[12]:


print(list(e2f.keys()))


# In[ ]:


Question 13. Make a multilevel dictionary called life.
Use these strings for the topmost keys: 'animals', 'plants',
and 'other'. Make the 'animals' key refer to another dictionary 
with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key
refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'.
Make all the other keys refer to empty dictionaries.


# In[13]:


life = {
    'animals':{
        'cats':['Henri','Grumpy','Lucy'],
        'octopi':{},
        'emus':{}
    },
    'plants':{},
    'other':{}
}
print(life)


# In[ ]:


Question 14. Print the top-level keys of life.


# In[14]:


print(list(life.keys()))


# In[ ]:


Question 15. Print the keys for life['animals'].


# In[15]:


print(list(life['animals'].keys()))


# In[ ]:


Question 16. Print the values for life['animals']['cats']


# In[16]:


print(life['animals']['cats'])

