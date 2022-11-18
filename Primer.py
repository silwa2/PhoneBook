from random import *
from time import sleep
import sys
import os

os.system('cls||clear')
def print_new(a):
    for c in a: 
        print (c, end = '')
        sys.stdout.flush() 
        sleep(0.09)
    print()

print_new('WELCOME TO THE PHONEBOOK DIRECTORY')

 
# creating a .txt file to store contact details 
filename = "555.txt" 
myfile = open(filename, "a+") 
myfile.close 
 
# defining main menu 
def main_menu(): 
    
    print_new( "\nMAIN MENU\n") 
    print_new( "1. Show all existing Contacts") 
    print_new( "2. Add a new Contact") 
    print_new( "3. Search the existing Contact") 
    print_new( "4. Exit") 
    
    choice = input("Enter your choice: ")
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print_new( "There is no contact in the phonebook.") 
        else: 
            print_new(filecontents) 
        myfile.close 
        enter = input("Press Enter to continue ...") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Press Enter to continue ...")
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Press Enter to continue ...") 
        main_menu() 
    elif choice == "4": 
        print_new("Thank you for using Phonebook!") 
    else: 
        print_new( "Please provide a valid input!\n") 
        enter = input( "Press Enter to continue ...") 
        main_menu() 
file = "111.txt" 
# defining search function         
def searchcontact(): 
    searchname = input( "Enter First name for Searching contact record: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname not in line: 
            print_new( "Your Required Contact Record is:", end = " ") 
            print_new( line)
            file.append(line)
            found = True 
             
    if found == False: 
        print_new( "The Searched Contact is not available in the Phone Book", searchname) 
 
# first name 
def input_firstname(): 
    first = input( "Enter your First Name: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# last name 
def input_lastname(): 
    last = input( "Enter your Last Name: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# storing the new contact details 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Enter your Phone number: ") 
    emailID = input( "Enter your E-mail Address: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print_new( "The following Contact Details:\n " + contactDetails + "\nhas been stored successfully!") 
 
main_menu() 
