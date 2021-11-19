b9067950-csc1034-A2
===

### 1.overview of the application
This package is build as the whole if the CSC1034: Portfolio-2.\
Enter `main.py` to view some useful information.

### 2.Assumptions I made when building this application
1.In the function menu, the user may enter the function name \
Solution, let users re-select

2.When adding a contact's phone number, the contact may enter letters by mistake\
Solution, let users re-select

### 3.How to run the application
run `main.py`
if there is not data(Person.data). it will create a new data
### 4.specific example "use case" :add
`*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit

\*****************************

Enter 1-6 to select the function to be performed:1\
Please enter the name of the contact:Name1\
Please enter contact phone number:1234567\
Please enter the addressNewcatle1\
Please enter birthday2021\
The contact has been added to the database\
There are(is) 1 contact(s) in total.\
name: Name1:('number:', '1234567', 'address:', 'Newcatle1', 'birthday:', '2021')\
`*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:1\
Please enter the name of the contact:\
No contact name entered\
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:1\
Please enter the name of the contact:Name1\
Unable to add, reason: the contact already exists.Choose 4 to modify the contact\
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:1\
Please enter the name of the contact:Name2\
Please enter contact phone number:one two three\
Please confirm the phone number format, it should be a pure number or number with \
please enter contact phone number: 1231234\
Please enter the addressNewcastle2\
Please enter birthday1000\
The contact has been added to the database\
There are(is) 2 contact(s) in total.\
name: Name1:('number:', '1234567', 'address:', 'Newcatle1', 'birthday:', '2021')\
name: Name2:('number:', '1231234', 'address:', 'Newcastle2', 'birthday:', '1000')
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:1\
Please enter the name of the contact:Name3\
Please enter contact phone number:+4412345566\
Please enter the address\
Please enter birthday\
The contact has been added to the database\
There are(is) 3 contact(s) in total.\
name: Name1:('number:', '1234567', 'address:', 'Newcatle1', 'birthday:', '2021')\
name: Name2:('number:', '1231234', 'address:', 'Newcastle2', 'birthday:', '1000')\
name: Name3:('number:', '+4412345566', 'address:', '', 'birthday:', '')
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:1\
Please enter the name of the contact:Name4\
Please enter contact phone number:\
Please confirm the phone number format, it should be a pure number or number with \
please enter contact phone number: 23456789\
Please enter the address\
Please enter birthday123\
The contact has been added to the database\
There are(is) 4 contact(s) in total.\
name: Name1:('number:', '1234567', 'address:', 'Newcatle1', 'birthday:', '2021')\
name: Name2:('number:', '1231234', 'address:', 'Newcastle2', 'birthday:', '1000')\
name: Name3:('number:', '+4412345566', 'address:', '', 'birthday:', '')\
name: Name4:('number:', '23456789', 'address:', '', 'birthday:', '123')
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:2
There are(is) 4 contact(s) in total.
name: Name1:('number:', '1234567', 'address:', 'Newcatle1', 'birthday:', '2021')
name: Name2:('number:', '1231234', 'address:', 'Newcastle2', 'birthday:', '1000')
name: Name3:('number:', '+4412345566', 'address:', '', 'birthday:', '')
name: Name4:('number:', '23456789', 'address:', '', 'birthday:', '123')
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:3
Enter the name of the contact you need to find:Name1
Name1:('number:', '1234567', 'address:', 'Newcatle1', 'birthday:', '2021')
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:4
Enter the name of the contact you want to delete:Name1
Successfully deleted!
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:2\
There are(is) 3 contact(s) in total.\
name: Name2:('number:', '1231234', 'address:', 'Newcastle2', 'birthday:', '1000')\
name: Name3:('number:', '+4412345566', 'address:', '', 'birthday:', '')\
name: Name4:('number:', '23456789', 'address:', '', 'birthday:', '123')\
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:5\
Enter the name of the contact that needs to be modifiedName3\
Please enter the new number:123456789\
Please enter the new addressNewcastle123\
Please enter new birthdayN/a
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:2\
There are(is) 3 contact(s) in total.\
name: Name2:('number:', '1231234', 'address:', 'Newcastle2', 'birthday:', '1000')\
name: Name4:('number:', '23456789', 'address:', '', 'birthday:', '123')\
name: Name3:('number:', '123456789', 'ass:', 'Newcastle123', 'bd:', 'N/a')\
*****************************
1. Add a contact
2. Show all contacts
3. Find a contact
4. delete a contact
5. Change contact information
6. quit
*****************************
Enter 1-6 to select the function to be performed:6

Process finished with exit code 0
