import os
import model
import view

filename = "myphonebook.txt" 
myfile = open(filename, "a+", encoding='utf-8') 
myfile.close 


# Команды меню
def commands ():
    choice = input("Введите команду: ")
    if choice == "1": 
        myfile = open(filename, "r+", encoding='utf-8') 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "В телефонной книге нет контактов.") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите ENTER для продолжения ...") 
        view.main_menu()
    elif choice == "2": 
        view.newcontact() 
        enter = input("Нажмите ENTER для продолжения ...") 
        view.main_menu()
    # elif choice == "5": 
    #     vuew.delcontact() 
    #     enter = input("Нажмите ENTER для продолжения ...") 
    #     view.main_menu() 
    elif choice == "3": 
        view.searchcontact() 
        enter = input("Нажмите ENTER для продолжения ...") 
        view.main_menu() 
    elif choice == "4": 
        model.print_new("Благодарим Вас за использование телефонной книги!")
    else: 
        model.print_new( "Пожалуйста, предоставьте правильные входные данные!\n") 
        enter = input( "Нажмите ENTER для продолжения ...") 
        view.main_menu()
        os.system('cls||clear')

        
    

 

