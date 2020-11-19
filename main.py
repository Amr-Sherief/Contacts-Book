import mysql.connector
import colors as cl

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='19371937A',
    database="Contact"
)

mycursor = mydb.cursor()

print(cl.color("Choose one of these options using numbers:", fg="yellow"))
print(cl.color("1: Insert a new contact", fg="red"))
print(cl.color("2: Search for the number of a contact", fg="red"))

insert = input()
i = 0

try:
    if insert == "1":  # Acts if the client chooses the first choice

        while i == 0:  # i = 0 is used to break or continue the looping (while) statement

            i = 0

            print(cl.color("Type the First Name and the Last Name of the Contact with space in between", fg="blue"))

            insert_1 = input()  # the input of the name of the contact

            insert_1_list = insert_1.split()

            First_Name = insert_1_list[0]  # the first name of the contact
            First_Name = First_Name.upper()  # capitalizes the string

            Last_Name = insert_1_list[1]  # the last name of the contact
            Last_Name = Last_Name.upper()  # capitalizes the string

            print(cl.color("Are you sure the name is " + First_Name + " " + Last_Name + " " + "(y/n)", fg="blue"))

            why = input()  # the input of the client that should be "y" or "n"

            if why == "y" or why == "Y":  # Acts if the client inserted "y" (yes)

                print(cl.color("Please insert the phone number of the contact", fg="blue"))

                phone = str(input())  # the phone number of the contact
                sql = "INSERT INTO contacts (First_Name, Last_Name, phone) VALUES (%s, %s, %s)"
                # the string which contains the sql code including placeholders for the values that should be inserted
                # remark We already created a table called (Contacts)

                sql_2 = (First_Name, Last_Name, phone)  # A Tuple for the execution of the sql code
                mycursor.execute(sql, sql_2)
                # executes the (sql) code withe the tuple (sql_2) as a list of placeholders
                mydb.commit()  # to save the changes in the sql database

                print(cl.color("Done!", fg="yellow"))

                i = 1

            elif why == "n" or why == "n":
                i = 0
                print(cl.color("Try Again! \n", fg="yellow"))

            else:
                print(cl.color("You should insert 'y' (Yes) or 'n' (No)", fg="yellow"))
                print("")
                i = 0

    elif insert == "2":
        print(cl.color("Insert the First name and Last name of the contact with space in between", fg="blue"))

        insert_1 = input()  # the input of the name of the contact

        insert_1_list = insert_1.split()

        First_Name = insert_1_list[0]  # the first name of the contact
        First_Name = First_Name.upper()  # capitalizes the string

        Last_Name = insert_1_list[1]  # the last name of the contact
        Last_Name = Last_Name.upper()  # capitalizes the string

        sql = "select phone from contacts where First_Name = %s and Last_Name = %s"
        # the string with the code to run in mysql database

        sql_2 = (First_Name, Last_Name)  # the placeholders for the mysql database code
        mycursor.execute(sql, sql_2)  # execute the mysql code

        myresult = mycursor.fetchone()  # returns the phone number of the contact

        print(cl.color("The number of the selected contact is:", fg="blue"))

        for row in myresult:  # prints the phone number of the contact
            print(cl.color(row, fg="yellow"))
except ValueError:
    print(cl.color("please insert numbers or text when you are told to", fg="yellow"))
except IndexError:
    print(cl.color("Please insert the name of the contact with space in between", fg="yellow"))
