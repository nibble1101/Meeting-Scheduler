import time
import sys
import userLogin
import newUser
#import newUser, existingUser

debug = True


def welcomeMessage():
    
    if debug == True:
        delayTime = 0
    elif debug == False:
        delayTime = 0.1
    
    print('\n\n********************************************************************\n\n')
    text = 'Welcome to the meeting scheduler:'
    for char in text:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(delayTime)
    print('\n\n********************************************************************')
    
    text = '\n\nPlease select option from the menu.\n\n'
    for char in text:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(delayTime)

    print('1: Existing User.')
    print('2: New User.\n')
    choice = int(input())

    if choice == 1:
        infoDict = userLogin.login()
    else:
        newUser.create()
        infoDict = userLogin.login()
    
    return infoDict


# if debug==True:
#     welcomeMessage()
# else:
#     pass