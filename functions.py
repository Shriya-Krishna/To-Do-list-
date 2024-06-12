"""A collection of function for doing my project."""

#Declaring  functions that will be used later

def remove_Items():  #this will remove items from list
    """
    Removes items from the global ToDoList based on user input.
    
    Prompts the user to enter the number of the item to be removed.
    Continues until the user types '0'. Handles invalid inputs and ensures
    the entered number is within the list range.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("When you are done, please type 0")
    outputs = [] 
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
        
def edits():  #this will edit items in the list
    """
    Edits items in the global ToDoList based on user input.
    
    Prompts the user to enter the number of the item to be edited and the new value.
    Continues until the user types '0' or 'done'. Handles invalid inputs and ensures
    the entered number is within the list range.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("IF FINISHED")
    print("Type done to the question: 'What would you like to change it to?'")
    print("Type 0 to the question: 'What number item would you like to edit?'")
    print("Please edit things to your To-Do List", "\n")
    while True:  # keeps on running until the break statement
        num = int(input("What number item would you like to edit? "))  # Asks the number to be edited.
        if num == 0:  # this is how the user can exit the edit thing.
            break
        thing = input("What would you like to change it to? ").strip().capitalize()  # strip takes out extra spaces. Capitalize makes the first letter capital.
        if thing.lower() == "done":
            break  # how user exits the thing
        if num <= len(ToDoList) and num > 0:  # if the number is within the length of the list
            ToDoList[num - 1] = thing  # lists are 0-indexed so we need to subtract 1 from the number the user inputted
        else:
            print("That is not a valid number. Try again.")
            continue  # asks for user input again for num and thing


def adding_Items():
    """
    Adds items to the global ToDoList based on user input.
    
    Prompts the user to add items, ensuring no duplicates are added.
    Continues until the user types 'done'.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("This list does not accept any duplicates!")
    while True:
        more = input("Please add an item here: ").strip().capitalize()  # takes out extra spaces and make the first letter capital
        if more.lower() == "done":  # to get user to exit the loop
            break
        if more not in ToDoList:  # if the item is not in the list it will add it. Deals with duplicacy
            ToDoList.append(more)  # this will add more items to the list

def print_List():
    """
    Prints the current global ToDoList with indexed numbers.
    
    Each item in the ToDoList is printed on a new line with its corresponding index.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    print("\n" * 2)  # for initial new lines so things don't get smushed together
    for index in range(len(ToDoList)):
        print(f"{index + 1}: {ToDoList[index]}")
        print()  # for a space # this will print the list.
