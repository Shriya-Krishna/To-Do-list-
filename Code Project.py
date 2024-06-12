#!/usr/bin/env python
# coding: utf-8

# In[19]:


#importing programs that I will use
import time
import os
import datetime
import calendar

#declaring variables to use later
adding = ""
editing = ""
remove = ""
done = ""
index = 0


# In[2]:


#Declaring  functions that will be used later
def removeItems():  #this will remove items from list
    print("When you are done, please type 0")
    while True:  #keeps on running until the break statement
    delete = int(input("Type the number of the item you would like to remove "))
    if delete == 0:
        break  #this is there if the user wants to break the statement.
    if delete <= len(ToDoList):  #if the item is in the list it will remove it
        del ToDoList[delete - 1]  #for 0-indexing
        print("Item has been deleted")
    else:  #if item is greater than the length of the list
        print("That item is not in your list. Try again.")
        continue  #it is going to go and ask for userinput for the remove variable again.


# In[21]:


def test_removeItems():
    # Test Case 1: Removing a single item
    ToDoList = ["Task 1", "Task 2", "Task 3"]
    inputs = [2, 0]  # Remove "Task 2"
    assert removeItems(ToDoList.copy(), inputs) == ["Task 1", "Task 3"], "Test Case 1 Failed"


# In[22]:


def edits():  #this will edit items in the list
    print("IF FINISHED")
    print("Type done to the question: 'What would you like to change it to?'")
    print("Type 0 to the question: 'What number item would you like to edit?'")
    print("Please edit things to your To-Do List", "\n")
    while True:  #keeps on running until the break statement
        num = int(input("What number item would you like to edit? "))  #Asks the number to be edited.
        if num == 0:  #this is how the user can exit the edit thing.
            break
        thing = input("What would you like to change it to? ").strip().capitalize()  #strip takes out extra spaces. Capitalize makes the first letter capital.
    if thing == "done" or thing == "Done":
        break  #how user exits the thing
    if num <= len(ToDoList):  #if the number is greater than the length of the list
        ToDoList[num -1] = thing  #lists are 0-indexed so we need to subtract 1 from the number the user inputted
    else:
        print("That is not a valid number. Try again.")
        continue  #asks for userinput again for num and thing


# In[23]:


def test_edits():
    # Test Case 1: Editing a single item
    ToDoList = ["Task 1", "Task 2", "Task 3"]
    inputs = [2, "new task 2", 0]  # Edit "Task 2"
    expected = ["Task 1", "New task 2", "Task 3"]
    assert edits(ToDoList.copy(), inputs) == expected, "Test Case 1 Failed"


# In[24]:


def addingItems():
    print("This list does not accept any duplicates!")
    while True:
        more = input("Please add an item here: ").strip().capitalize()  #takes out extra spaces and makes the first letter capital
        if more == "done" or more == "Done":  #to get user to exit the loop
            break
        if more not in ToDoList:  #if the item is not in the list it will add it. Deals with duplicacy
            ToDoList.append(more)  #this will add more items to the list


# In[25]:


def test_addingItems():
    # Test Case 1: Adding a single item
    ToDoList = ["Task 1", "Task 2"]
    inputs = ["Task 3", "Done"]  # Add "Task 3"
    expected = ["Task 1", "Task 2", "Task 3"]
    assert addingItems(ToDoList.copy(), inputs) == expected, "Test Case 1 Failed"


# In[26]:


def printList():
    "\n"  #for a new line so things don't get smushed together
    for index in range(len(ToDoList)):
        print(f"{index+1}: {ToDoList[index]}")
        print()  # for a space #this will print the list.


# In[27]:


def test_printList():
    # Test Case 1: Printing a list with multiple items
    ToDoList = ["Task 1", "Task 2", "Task 3"]
    expected_output = "1: Task 1\n\n2: Task 2\n\n3: Task 3\n\n"
    assert printList(ToDoList) == expected_output, "Test Case 1 Failed"


# In[28]:


#Intro to the program
ToDoList = []
intro = "📋Welcome to ToDo List Manager!📋"
print(f"\033[1;34m{intro:^50}")  #for formatting settings like put it in center and stuff.
print("Please add items to your To-Do List, one at a time.")
print("Type 'done' when you are finished adding items. ", "\n")

addingItems()  #calling the addingItems
time.sleep(0.5)  #making the program wait for 0.5 seconds
os.system("clear")  #clearing the screen

printList()  #calling printList to print the list to the user.


# In[29]:


while True:
    print("Type 'add' to add items")
    print("Type 'edit' to edit items")
    print("Type 'remove' to remove items,")
    print("Type 'exit' when you are done", "\n")
    action = input("Would you like to add, edit, remove items or exit from your list? ").strip().capitalize()  #strip and capilize is there to take away extra spaces and capitalize the first letter of the word.
    print()  #just for an extra space
    if action == "Exit":
        break  #to exit the loop
    elif action == "Add":
        addingItems()  #calling adding Items function
        printList()  #print list
    elif action == "Edit":
        edits()  #calling edits function
        printList()
    elif action == "Remove":
        removeItems()  #calling remove Items function
        printList()
    else:
        print("Sorry, but that is an invalid input. Please try again.")
        continue
time.sleep(0.5)
os.system("clear")
print("Okay, here comes the not-so-fun part!")
print("You get to put due dates!!")
"\n"
year = int(input("🗓️ What year is it? 🗓️ "))
month = int(input("📆 What month is it? (1-12) 📆 "))
print()  #empty prints for spaces
print()
print()
print("Now that you have the calendar dates infront of you....")
print("LET'S GET STARTED!")
print()
print()


# In[30]:


for index in range(len(ToDoList)):  #for item in the To Do list. len gives you the length of the To-Do list.
    global formattedDate, formattedTime  #global variables. they are used througout the program.
    print(calendar.month(year, month))  #uses the year and the month to print the calendar.
    print()  #new lines
    print()
    print()
    print(f"{index+1}: {ToDoList[index]}")  #gives the user the task.

    while True:
        date = int(input("What date is this due? "))
        if date < 32:
            break
        else:  #deals with invalid dates
            print("That is not a valid date. Try again.")
            continue
    while True:
        hour = int(input("What hour is this due? Please enter integers only: "))
        if hour < 13:
            break
        else:  #deals with invalid time
            print("Please do not enter 24 hour time.")
            continue
    while True:
        min = int(input("What minute is this due? Please enter integers only: "))
        if min < 60:
            break
        else:  #deals with invalid mins
            print("Try again. Please do not enter more than 60 minutes.")
            continue
    while True:
    amPm = input("am or pm? ")
        if amPm != "am" or amPm != "pm":
            break
        else:  #deals with human error
            print("Please try again. Please enter am or pm.")
            continue
    timings = datetime.datetime(year, month, date, hour, min)  #this variable now has all the info.

    time.sleep(0.5)  #the system stops for 0.5 seconds
    os.system("clear")  #the system clears the screen.

    formattedDate = timings.strftime("%Y, %B, %d, (%A)")  #this is the format of the date.
    
    formattedTime = timings.strftime("%X")  #this is the format of the time.
    
    ToDoList[index] = {  #I have put dictionaries in each index of the Todolist. because it doesn't work otherwise. 
          "task":ToDoList[index],  #the key task refers to the task in the To-Do list
          "due_date":formattedDate,  #the key due_date refers to the due date. 
          "due_time":formattedTime,  #the key due_time refers to the due time. 
          "am_pm": amPm}  #the key am_pm refers to the am or pm. 

    print(f"Your task {ToDoList[index]['task']} is due on {ToDoList[index]['due_date']} at {ToDoList[index]['due_time']} {ToDoList[index]['am_pm']}")
    print()
    print()  #spaces
    
print("Now your final To-Do List will be printed.")
time.sleep(0.5)  #system stops for 0.5 seconds
os.system("clear")  #system clears the screen

finalIntro = "📋Final To-Do List!📋"  #final list being printed.
print()
print("\033[0;35m", "\033[1m",f"{finalIntro:^50}")  #again formatting and color changing.


# In[31]:


for index in range(len(ToDoList)):  #Now it's printing the whole list using the keys.
    print(f"Your task {ToDoList[index]['task']} is due on {ToDoList[index]['due_date']} at {ToDoList[index]['due_time']} {ToDoList[index]['am_pm']}")
    print()  #space for formatting
exit()  #exiting the program

