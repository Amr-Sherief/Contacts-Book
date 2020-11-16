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

while True:
    if insert == "1":                                # Acts if the client chooses the first choice
        print("Type the First Name and the Last Name of the Contact with space in between")
        insert_1 = input()
        insert_1_list = insert_1.split()
        First_Name = insert_1_list[0]
        Last_Name = insert_1_list[1]
        print("Are you sure the name is " + First_Name + " " + Last_Name + "((y/n))")
        insert_2 = input()
        if insert_2 == "y" or "Y":
            print("Please insert the phone number of the contact")
            phone = int(input())
        elif insert_2 == "n" or "N":
            continue

# remark We already created a table called (Contacts)

mycursor.execute("")

# todo add a try/else if a value error is raised
# todo Complete if insert_2 == y
# todo add comments
