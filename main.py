import mysql.connector
import colors

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='19371937A',
    database="Contact"
)

mycursor = mydb.cursor()

print("Choose one of these options using numbers:")
print("1: Insert a new contact")
print("2: Search for the number of a contact")

insert = input()
i = 0

if insert == "1":                                     # Acts if the client chooses the first choice

    while i == 0:                                     # i = 0 is used to break or continue the looping (while) statement

        i = 0

        print("Type the First Name and the Last Name of the Contact with space in between")

        insert_1 = input()                            # the input of the name of the contact

        insert_1_list = insert_1.split()

        First_Name = insert_1_list[0]                 # the first name of the contact
        Last_Name = insert_1_list[1]                  # the last name of the contact

        print("Are you sure the name is " + First_Name + " " + Last_Name + " " + "(y/n)")

        why = input()         # the input of the client that should be "y" or "n"

        if why == "y" or why == "Y":           # Acts if the client inserted "y" (yes)

            print("Please insert the phone number of the contact")

            phone = str(input())               # the phone number of the contact
            sql = "INSERT INTO contacts (First_Name, Last_Name, phone) VALUES (%s, %s, %s)"
            # the string which contains the sql code including placeholders for the values that should be inserted
            # remark We already created a table called (Contacts)

            sql_2 = (First_Name, Last_Name, phone)           # A Tuple for the execution of the sql code
            mycursor.execute(sql, sql_2)
            # executes the (sql) code withe the tuple (sql_2) as a list of placeholders
            mydb.commit()                                    # to save the changes in the sql database

            print("Done!")

            i = 1

        elif why == "n" or why == "n":
            i = 0
            print("Try Again! \n")

        else:
            print("Please insert 'y' (Yes) or 'n' (No) and insert your first name and last name with space in between")
            print("")
            i = 0

elif insert == "2":
    print("Insert the First name and Last name of the contact with space in between")

    insert_1 = input()  # the input of the name of the contact

    insert_1_list = insert_1.split()

    First_Name = insert_1_list[0]  # the first name of the contact
    Last_Name = insert_1_list[1]  # the last name of the contact
    sql = "select phone from contacts where First_Name = %s and Last_Name = %s"
    sql_2 = (First_Name, Last_Name)

    mycursor.execute(sql, sql_2)

    myresult = mycursor.fetchone()

    print("The number of the selected contact is:")

    for row in myresult:
        print(row)

# todo add a try/else if a value error is raised
# todo Complete if insert_2 == y
# todo add comments
# todo add a try/else if an Index Error happens in line 25
# todo add colored text
# todo a capitalization code so that if the input of the client was in upper or lower case the code runs properly
