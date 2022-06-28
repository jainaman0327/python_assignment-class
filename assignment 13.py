#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1. What advantages do Excel spreadsheets
get_ipython().set_next_input('have over CSV spreadsheets');get_ipython().run_line_magic('pinfo', 'spreadsheets')

Ans: The Advantages of Excel over CSV are:

1.Excel (XLS and XLSX) file formats are better for
storing and analysing complex data.

2.An Excel not only stores data but can also do
operations on the data using macros, formulas etc

3.CSV files are plain-text files, Does not contain formatting, formulas, macros, etc.
It is also known as flat files


# In[ ]:


Question 2.What do you pass to csv.reader() and csv.writer() to
get_ipython().set_next_input('create reader and writer objects');get_ipython().run_line_magic('pinfo', 'objects')


# In[ ]:


import csv
with open('text.csv','r') as file:
    csv_file = csv.reader(file,delimiter=',')
    for ele in csv_file:
        print(ele)


# In[ ]:


Question 3. What modes do File objects for reader and
get_ipython().set_next_input('writer objects need to be opened in');get_ipython().run_line_magic('pinfo', 'in')

Ans: For csv.reader(iterable_file_object), 
the file objects needed to be opened in read 
mode mode='r' Whereas for csv.writer(iterable_file_object) 
the file objects needed to be opened in write mode mode='w'


# In[ ]:


get_ipython().set_next_input('Question 4. What method takes a list argument and writes it to a CSV file');get_ipython().run_line_magic('pinfo', 'file')

Ans: csv.writer class provides two methods for writing to CSV.
They are writerow() and writerows(). writerow() method writes a
single row at a time. Whereas writerows() method is used to write
multiple rows at a time.


# In[ ]:


# Example Program
import csv      
fields = ['Name', 'Branch', 'Year', 'CGPA'] #column names 
rows = [ 
            ['Nikhil', 'COE', '2', '9.0'],  # data rows of csv file 
            ['Sanchit', 'COE', '2', '9.1'], 
            ['Ravi', 'IT', '2', '9.3']
       ] 
with open("university_records.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) # creating a csv writer object 
    csvwriter.writerow(fields) # writing the fields 
    csvwriter.writerows(rows) # writing the data rows 


# In[ ]:


Question 5. What do the keyword arguments
get_ipython().set_next_input('delimiter and line terminator do');get_ipython().run_line_magic('pinfo', 'do')

Ans: Lets take the example of a csv file:
First Name, Last Name, Age
Mano, Vishnu, 24
Vishnu, Vardhan, 21
Here ',' is Delimiter. We can use any Character
as per our needs if required. Similarly Line Terminator 
comes at end of line by default it is newline and can be
changed accourding to Requirement.


# In[ ]:


Question 6. What function takes a string of JSON data and returns
get_ipython().set_next_input('a Python data structure');get_ipython().run_line_magic('pinfo', 'structure')

Ans: loads() method takes a string of JSON data and returns
a Python data structure


# In[2]:


# Example of json.loads() method
import json
my_details_json ='''{
    "Name": "aman jain",
    "Qualification": "Bachelor of science",
    "Stream": "Computer Science"
}'''
print(my_details_json)
print(f'Type of my_details_json is {type(my_details_json)}')
my_details = json.loads(my_details_json)
print(my_details)
print(f'Type of my_details is {type(my_details)}')


# In[ ]:


Question 7. What function takes a Python data structure
get_ipython().set_next_input('and returns a string of JSON data');get_ipython().run_line_magic('pinfo', 'data')

Ans: dumps() method takes a python data structure and 
    returns a string of JSON data


# In[3]:


# Example of json.dumps() method
import json
my_details = {
    'Name':'aman jain',
    'Stream':'Computer Science',
    'Qualification':'Bachelor of science'
}
print(my_details)
print(f'Type of my_details is {type(my_details)}')
my_details_json = json.dumps(my_details, indent=4, sort_keys=True)
print(my_details_json)
print(f'Type of my_details_json is {type(my_details_json)}')

