""" This is a command line calendar - whatever that is..."""

from time import sleep, strftime
import datetime as dt

NAME = "Tyrone"

calendar = {}

base = dt.date.today()
date_list = [base + dt.timedelta(days=x) for x in range(0, 5)]
  
calendar = dict.fromkeys(date_list, [""])

def welcome():
  print ("Welcome %s to Calendar!" % NAME)
  print ("calendar is opening")
  sleep(1)
  print ("Today is: " + strftime("%A %B %d %Y"))
  print ("Time is: " + strftime("%X"))
  sleep(1)
  print ("what would you like to do?")
                                 
def start_calendar():  
  welcome()
  start = True
  while start:
    user_choice = input("Add (A), Update (U), View (V), Delete (D), Exit (X)")
    user_choice = user_choice.upper()
    
    if user_choice == "V":
      if len(calendar.keys()) < 1 :
        print ("calendar is currently empty")
      else:
        print (calendar)
    elif user_choice =="U":
      date = input("What date? ")
      update = input("Enter the update: ")
      calendar[date] = update
      print (calendar)
      
    elif user_choice =="A":    
      event = input("Enter event: ")
      date = input("What date? MM/DD/YYYY :")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print("I'm sorry that's not a valid format")
        try_again = input("Try Again? Y or N :")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print (calendar)
        
    elif user_choice =="D": 
       if len(calendar.keys()) < 1 :
        "calendar is currently empty"
       else:
          event = input("Enter event to remove: ")
          for date in list(calendar):
            if event == calendar[date]:
              del(calendar[date])
              print("delete successful")
              print (calendar)
              
    elif  user_choice =="X": 
      start = False
    else:
      print("please enter a valid choice")
      start = False
     
start_calendar()
    