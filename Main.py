#!/usr/bin/python3.7
if __name__ == '__main__':''

__author__ = 'fierce'
import re
import os
import pickle

Path = 'Person.data'  # Determine whether there is a database

if os.path.exists(Path) == False:  # there is not a database
    f = open((Path), 'wb')  # Open data in write binary mode
    temp = {'total': 0}  # Local variables, used to count the number of people
    pickle.dump(temp, f)  # Save the object temp to f
    f.close()  # close f
else:
    pass


# Add contacts
def add():  # Custom add function
    name = input('Please enter the name of the contact:')  # get the name data
    if name == "":
        print("No contact name entered")
    else:
        f = open((Path), 'rb')  # Open the file in read binary mode
        a = pickle.load(f)  # Read information from f in the form of an array
        f.close  # close f
        b = 0  # Custom local variables
        for key in a.keys():  # Cycle "key" is custom, "a.keys()" is all keys read out from the address book
            b += 1  # Increment of custom variables
            if key == name and b <= a['total'] + 1:  # Determine whether the conditions are met
                print("Unable to add, reason: the contact already exists.Choose 4 to modify the contact")
                break
            if b == a['total'] + 1 and key != name:  # Determine whether the conditions are met
                number = input("Please enter contact phone number:")
                while not re.match(r'[0-9,+,]', number):
                    print("Please confirm the phone number format, it should be a pure number or number with "+"")
                    number = input("please enter contact phone number: ")
                ass = input('Please enter the address')  # get the address
                birthday = input("Please enter birthday")  # get the birthday
                # Encapsulate numbers, birthdays and phone numbers into one data
                info = ("number:", number, "address:", ass, "birthday:",birthday)
                information = {name: info}  # Assign packaged data to name
                a['total'] += 1  # total＋1
                a.update(information)  # updata
                f = open((Path), 'wb')  # Open data in write binary mode
                pickle.dump(a, f)  # Write "a" object to f
                f.close()  # close f
                print('The contact has been added to the database')
                showall()
                break


# Show all contacts
def showall():  # Custom Showall function
    f = open((Path), 'rb')  # Open the file in read binary mode
    a = pickle.load(f)  # Read information from f in the form of an array
    print("There are(is) {} contact(s) in total.".format(a['total']))  # Show and count contacts
    for key in a.keys():  # Import the corresponding key in the name
        if key != 'total':
            print("name:", "{""}:{""}".format(key, a[key]), )  # Show all contacts
    f.close


# find contact
def search(name):  # Custom search function
    f = open((Path), 'rb')
    a = pickle.load(f)  # Read information from f in the form of an array
    b = 0
    for key in a.keys():  # Import the corresponding key in the name
        b += 1  # Increment of custom variables
        if key == name and b <= a['total'] + 1:  # Check if there is this contact
            print("{""}:{""}".format(name, a[key]))  # print this contact imformation
            break
        if b == a['total'] + 1 and key != name:  # this is not this contact
            print("Contact does not exist")  # Tell the user that there is no information for this contact
            break


# delete contact
def deleate(name):  # Custom deleate function
    f = open((Path), 'rb')
    a = pickle.load(f)
    f.close()
    b = 0
    for key in a.keys():
        b += 1
        if key == name and b <= a['total'] + 1:
            a.pop(name)
            a['total'] -= 1
            f = open((Path), 'wb')
            pickle.dump(a, f)
            f.close()
            print("Successfully deleted!")
            break
        if b == a['total'] + 1 and key != name:
            print("failed to delete. Reason:This contact does not exist")
            break


def change(name):
    f = open((Path), 'rb')
    a = pickle.load(f)
    f.close()
    b = 0
    for key in a.keys():
        b += 1
        if key == name and b <= a['total'] + 1:
            a.pop(name)
            a['total'] -= 1
            f = open((Path), 'wb')
            pickle.dump(a, f)
            f.close()
            C_add(name)
            break

        if b == a['total'] + 1 and key != name:
            print("Failed to modify information, Reason:This contact does not exist")
            break


def C_add(name):
    f = open((Path), 'rb')
    a = pickle.load(f)
    f.close()
    b = 0
    for key in a.keys():
        b += 1
        if b == a['total'] + 1 and key != name:
            number = input('Please enter the new number:')
            while not re.match(r'[0-9,+,]', number):
                print('Please confirm the phone number format, it should be a pure number or number with"+" ')
                number = input("please enter the new contact phone number: ")
            ass = input('Please enter the new address')
            birthday = input("Please enter new birthday")
            info = ("number:", number, "ass:", ass, "bd:", birthday)
            information = {name: info}
            a['total'] += 1
            a.update(information)
            f = open((Path), 'wb')
            pickle.dump(a, f)
            f.close()
            break

def point():
    print("*****************************")
    print("1. Add a contact")
    print("2. Show all contacts")
    print("3. Find a contact")
    print("4. delete a contact")
    print("5. Change contact information")
    print("6. quit")
    print("*****************************")

while True:
    point()
    x = input("Enter 1-6 to select the function to be performed:")  # 获取输入
    if x == '1':
        add()
        continue
    if x == '2':
        showall()
        continue
    if x == '3':
        name = input("Enter the name of the contact you need to find:")
        search(name)  # Use the "search" function and pass a parameter: name
        continue
    if x == '4':
        name = input("Enter the name of the contact you want to delete:")
        deleate(name)  # Use the "deleate" function and pass a parameter: name
        continue
    if x == '5':
        name = input("Enter the name of the contact that needs to be modified")
        change(name)  # Use the "change" function and pass a parameter: name
        continue
    if x == '6':
        exec("quit()")
    else:
        print("Please enter only the numbers 1, 2, 3, 4, 5, 6")
        continue

