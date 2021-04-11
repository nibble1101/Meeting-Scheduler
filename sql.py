import psycopg2, bcrypt

#1 for checking user
#2 for registering user
def checkOrRegisterUser(option, di):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="admin",
            host="localhost",
            port="5432",
            database="meetingscheduler"
        )
        cursor = connection.cursor()
        if(option == 1):
            emailid = list(di.keys())[0]
            enteredPassword = list(di.values())[0].encode("utf-8")
            cursor.execute(f"SELECT passwords FROM users WHERE emailid = '{emailid}'")
            password = cursor.fetchall()
            if password == []:
                pass
            else:
                password = password[0][0]
            if password == [] or bcrypt.checkpw(enteredPassword, password.encode("utf-8")) != True:
                return False
            elif bcrypt.checkpw(enteredPassword, password.encode("utf-8")):
                return True
        
        elif(option == 2):
                passwords = di['passwords']
                cursor.execute(f"SELECT emailid FROM users WHERE emailid = '{di['emailid']}'")
                emailid = cursor.fetchall()
                if emailid == []:
                    cursor.execute(f"INSERT INTO users (first_name, last_name, phone, gender, emailid, passwords) VALUES ('{di['first_name']}', '{di['last_name']}', '{di['phone']}', '{di['gender']}', '{di['emailid']}', '{di['passwords'].decode('utf-8')}')")
                    print("Data has been written on the DB")
                    connection.commit()
                    return True
                
                else:
                    print("\nThe Email-ID is already used. Please try different Email-ID")
                    return False
                
    except ConnectionError:
        print("Connection Unsuccessful.")

