"""Classes used throughout project"""

while True:
  print("Type 'add' to add items")
  print("Type 'edit' to edit items")
  print("Type 'remove' to remove items,")
  print("Type 'exit' when you are done", "\n")
  action = input(
      "Would you like to add, edit, remove items or exit from your list? "
  ).strip().capitalize(
  )  #strip and capilize is there to take away extra spaces and capitalize the first letter of the word.
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

for index in range(
    len(ToDoList)
):  #for item in the To Do list. len gives you the length of the To-Do list.
  global formattedDate, formattedTime  #global variables. they are used througout the program.
  print(calendar.month(
      year, month))  #uses the year and the month to print the calendar.
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
  timings = datetime.datetime(year, month, date, hour,
                              min)  #this variable now has all the info.

  time.sleep(0.5)  #the system stops for 0.5 seconds
  os.system("clear")  #the system clears the screen.

  formattedDate = timings.strftime(
      "%Y, %B, %d, (%A)")  #this is the format of the date.
  formattedTime = timings.strftime("%X")  #this is the format of the time.
  ToDoList[
      index] = {  #I have put dictionaries in each index of the Todolist. because it doesn't work otherwise. 
          "task":
          ToDoList[index],  #the key task refers to the task in the To-Do list
          "due_date":
          formattedDate,  #the key due_date refers to the due date. 
          "due_time":
          formattedTime,  #the key due_time refers to the due time. 
          "am_pm": amPm  #the key am_pm refers to the am or pm. 
      }
  print(  #I am now using the keys inside the To-Do list index to acess the values like the due date, time, am/pm stuff
      f"Your task {ToDoList[index]['task']} is due on {ToDoList[index]['due_date']} at {ToDoList[index]['due_time']} {ToDoList[index]['am_pm']}"
  )
  print()
  print()  #spaces
print("Now your final To-Do List will be printed.")
time.sleep(0.5)  #system stops for 0.5 seconds
os.system("clear")  #system clears the screen

finalIntro = "📋Final To-Do List!📋"  #final list being printed.
print()
print("\033[0;35m", "\033[1m",
      f"{finalIntro:^50}")  #again formatting and color changing.

for index in range(
    len(ToDoList)):  #Now it's printing the whole list using the keys.
  print(
      f"Your task {ToDoList[index]['task']} is due on {ToDoList[index]['due_date']} at {ToDoList[index]['due_time']} {ToDoList[index]['am_pm']}"
  )
  print()  #space for formatting

exit()  #exiting the program
