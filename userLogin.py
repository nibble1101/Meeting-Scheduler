import sys, sql, time, bcrypt

debug = True

def login():

    loginStatus = False

    if debug == True:
        delayTime = 0
    elif debug == False:
        delayTime = 0.1

    while loginStatus == False:

        text = '\n\nPlease enter your Email ID and password to Log In: '
        for char in text:
            print(char, end = "")
            sys.stdout.flush()
            time.sleep(delayTime)

        emailid = input('Email ID: ')
        password = input("Enter password: ")
        di = {
            emailid : password
        }
        loginStatus = sql.checkOrRegisterUser(1,di)

    text = '\n\nWelcome user.'
    for char in text:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(delayTime)



    #Now, search for the email ID in the csv file. Once the email ID is found, compare the password. If the password matches, store the information in the dictionary and then return it. Else show the prompt that email ID or password is incorrect. Then ask the user to re-enter it.




