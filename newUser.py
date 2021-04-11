import csv
import time
import sys, sql, bcrypt

debug = False

def create():
    if debug == True:
        delayTime = 0
    elif debug == False:
        delayTime = 0.1

    
    status = False

    

    print('\n\n********************************************************************\n\n')
    text = 'Welcome to the meeting scheduler:'
    print(text)
    print('\n\n********************************************************************')

    while status != True:
        di = {}
        text = '\n\nPlease fill the info to register:'
        for char in text:
            print(char, end = "")
            sys.stdout.flush()
            time.sleep(delayTime)

        text = '\n\nPlease enter your First Name: '
        for char in text:
            print(char, end = "")
            sys.stdout.flush()
            time.sleep(delayTime)
        if debug==True:
            firstName = "Amyra"
        else:
            firstName = input()
        
        text = '\n\nPlease enter your Last Name: '
        for char in text:
            print(char, end = "")
            sys.stdout.flush()
            time.sleep(delayTime)
        if debug==True:
            lastName = "Agarwal"
        else:
            lastName = input()

        text = '\n\nPlease enter your phone number: '
        for char in text:
            print(char, end = "")
            sys.stdout.flush()
            time.sleep(delayTime)
        if debug==True:
            number = 4253728098
        else:
            number = float(input())
        
    
        text = '\n\nPlease enter your gender as MA for male, FA for female and NA for not disclosing it: '
        for char in text:
            print(char, end = "")
            sys.stdout.flush()
            time.sleep(delayTime)
        if debug==True:
            gender = 'FA'
        else:
            gender = input()

        text = '\n\nPlease enter your email ID: '
        for char in text:
            print(char, end = "")
            sys.stdout.flush()
            time.sleep(delayTime)
        if debug==True:
            emailid = "amyra@gmail.com"
        else:
            emailid = input()

        text = '\n\nPlease enter a password: '
        for char in text:
            print(char, end = "")
            sys.stdout.flush()
            time.sleep(delayTime)
        if debug==True:
            password = bcrypt.hashpw(b'Amyra12', bcrypt.gensalt())
        else:
            password = bcrypt.hashpw(input().encode("utf-8"), bcrypt.gensalt())

        di = {
            'first_name' : firstName,
            'last_name' : lastName,
            'phone' : number,
            'gender' : gender,
            'emailid' : emailid,
            'passwords' : password
        }
        status = sql.checkOrRegisterUser(2, di)
        if status == True:
            text = '\n\nThank you for registering... '
            for char in text:
                print(char, end = "")
                sys.stdout.flush()
                time.sleep(delayTime)

        

    #Now we will write the user data to the file userData and then just simply return from the function.







