#!/usr/bin/env python
# coding: utf-8

# # Project Description

# Write a brief description of your project here. 
# 
# Note that projects should be self-sufficient, so make sure to provide enough information and context here for someone to understand what you are doing in your project, and why. 

# In[45]:


#Intro to the program
# The ToDo List Manager program offers a comprehensive solution for managing tasks efficiently. As users add items to their to-do list, the program automatically checks for duplicates and incorporates the new items seamlessly. Utilizing the OS and time libraries, the screen is cleared to display the updated list. Users can then choose to add more items, edit existing ones, remove items, or exit the program. Each of these options is handled by specific functions within a continuous loop, allowing for ongoing modifications until the user is satisfied.
# When editing the list, users simply provide the task number they wish to change and are prompted to update the item. For removing tasks, the user is guided through the deletion process. Upon choosing to exit, users are prompted to assign due dates to each task. This section leverages the calendar library to display the monthly calendar based on the inputted year and month, helping users to accurately set due dates. The program then prompts users to enter the date, hour, minute, and AM/PM for each task. It ensures valid inputs by requesting the re-entry of incorrect values.
# All these inputs are organized into the to-do list by storing each task’s details in a dictionary. Finally, the program prints out each task with its respective due date and time, using a loop for clear presentation. Throughout the process, the program handles user inputs smoothly by starting indexes from one, avoiding the need for zero-based indexing. This results in a user-friendly experience, providing a detailed and easily navigable to-do list with specific due dates and times for each task.
# In the file Code Project a full exmaple of my code running can be seen. All my code is located there. 


# In[46]:


#NOTE: chatgpt was used to generate numpy style doc strings; docstrings were reviwed and generated after generated  


# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[30]:


from my_module.functions import remove_Items
from my_module.functions import edits
from my_module.functions import adding_Items
from my_module.functions import print_List


# In[31]:


def todo_list():
    return ["item1", "item2", "item3"]

def test_remove_items(todo_list, monkeypatch):
    print("Testing remove_Items function")
    inputs = iter([2, 0])  # Mock user inputs: remove the second item, then exit
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    print("Mock inputs set for remove_Items")
    updated_list, outputs = remove_Items(todo_list.copy())
    print(f"Updated list: {updated_list}")
    print(f"Outputs: {outputs}")
    assert updated_list == ["item1", "item3"]
    assert outputs == ["Item has been deleted"]


# In[32]:


from my_module.functions import remove_Items, edits, adding_Items, print_List


# In[35]:


get_ipython().system('pytest')


# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. Your Python Background
# 2. How your project went above and beyond the requirements of the project and/or how you challenged yourself to learn something new with the final project

# In[10]:


#I have no background in Python, but I challenged myself by learning about libraries. Libraries in Python are collections of pre-written code that you can import into your program to perform specific tasks. For my project, I utilized libraries like DateTime, calendar, os, and time. I went beyond the basic requirements by using the os library to clear the console for readability, incorporating the time library to allow users sufficient time to read console text, and implementing calendar and DateTime libraries to manage due dates and formatting. Additionally, I utilized f-strings for efficient printing and ANSI color codes for visual formatting.

