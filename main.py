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

if insert == "1":                                       # Acts if the client chooses the first choice

    while i == 0:

        i = 0

        print("Type the First Name and the Last Name of the Contact with space in between")

        insert_1 = input()

        insert_1_list = insert_1.split()

        First_Name = insert_1_list[0]
        Last_Name = insert_1_list[1]

        print("Are you sure the name is " + First_Name + " " + Last_Name + " " + "(y/n)")

        why = input()

        if why == "y":

            print("Please insert the phone number of the contact")

            phone = str(input())
            sql = "INSERT INTO contacts (First_Name, Last_Name, phone) VALUES (%s, %s, %s)"

            # remark We already created a table called (Contacts)

            sql_2 = (First_Name, Last_Name, phone)           # A Tuple for the execution of the sql code
            mycursor.execute(sql, sql_2)
            mydb.commit()                                    # to save the changes in the sql database

            print("Done!")

            i = 1

        if why == "n":
            i = 0


# todo add a try/else if a value error is raised
# todo Complete if insert_2 == y
# todo add comments
# todo add a try/else if an Index Error happens in line 25
# todo add colored text
