import calendar
from datetime import date
import time
import sys

def printCalendar() -> dict:

    if debug == True:
        delayTime = 0
    elif debug == False:
        delayTime = 0.1

    initialYear = date.today().year
    initialMonth = date.today().month
    print("\n\n")
    for i in range(0, (13-initialMonth)):
        print(calendar.month(initialYear, initialMonth+i))
    
    text = '\n\nPlease enter the Month: '
    for char in text:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(delayTime)
    monthInput = input()
    monthInput = int(monthInput)


    text = '\n\nPlease enter the Date: '
    for char in text:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(0.1)
    dateInput = input()
    dateInput = int(dateInput)

    scheduleDict = {
        'Date':dateInput,
        'Month':monthInput
    }
    return scheduleDict
