#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Quesetion 1. What does RGBA stand for');get_ipython().run_line_magic('pinfo', 'for')

Ans: RGBA is a four-channel format containing 
data for Red, Green, Blue, and an Alpha value.
Where Alpha Represents the Opacity


# In[ ]:


Question 2. From the Pillow module, how do you get
get_ipython().set_next_input('the RGBA value of any images');get_ipython().run_line_magic('pinfo', 'images')

Ans: ImageColor.getcolor() gives rgba value of any image


# In[ ]:


Question 3. What is a box tuple,
get_ipython().set_next_input('and how does it work');get_ipython().run_line_magic('pinfo', 'work')

Ans: A box tuple is a tuple value of four integers:
the left-edge x-coordinate, the top-edge y-coordinate,
the width, and the height, respectively.


# In[ ]:


Quesetion 4. Use your image and load in notebook then, 
get_ipython().set_next_input('How can you find out the width and height of an Image object');get_ipython().run_line_magic('pinfo', 'object')


# In[3]:


#Example Program
from PIL import Image
pic = Image.open('new.jpg.jpg')
print(f'Width, Height -> {pic.size}') # Approach 1
print(f'Width, Height -> {pic.width},{pic.height}') # Approach 2
width,height = pic.size
print(f'Width, Height -> {width},{height}') # Approach 3


# In[ ]:


Question 5. What method would you call to get Image
get_ipython().set_next_input('object for a 100×100 image, excluding the lower-left quarter of it');get_ipython().run_line_magic('pinfo', 'it')


# In[4]:


from PIL import Image 
img = Image.open('new.jpg.jpg')
new_img = img.crop((0,50,50,50))


# In[5]:


get_ipython().set_next_input('Question 6. After making changes to an Image object, how could you save it as an image file');get_ipython().run_line_magic('pinfo', 'file')


# In[6]:


#Example program
from PIL import Image 
pic = Image.open('new.jpg.jpg')
pic.save('new2.jpg')


# In[ ]:


get_ipython().set_next_input('Question 7. What module contains Pillow’s shape-drawing code');get_ipython().run_line_magic('pinfo', 'code')

Ans: Pillows ImageDraw module contains Shape drawing methods


# In[ ]:


Question 8. Image objects do not have drawing methods. 
get_ipython().set_next_input('What kind of object does? How do you get this kind of object');get_ipython().run_line_magic('pinfo', 'object')

Ans: ImageDraw objects have shape-drawing methods such as point(),
    line(), or rectangle().They are returned by passing
    the Image object to the ImageDraw.Draw() function.

