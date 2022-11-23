import controller
import model
import os

filename = "myphonebook.txt" 
myfile = open(filename, "a+", encoding='utf-8') 
myfile.close 

def main_menu(): 
    os.system('cls||clear') 
    model.print_new( "Добро пожаловать в телефонный справочник")
    model.print_new( "\nМЕНЮ СПРАВОЧНИКА\n") 
    model.print_new( "1. Показать все существующие контакты") 
    model.print_new( "2. Добавить новый контакт") 
    model.print_new( "3. Найти контакт") 
    model.print_new( "4. Выход") 
    # model.print_new ( "5. Удалить контакт")
    controller.commands()

# поиск информации        
def searchcontact(): 
    searchname = input("Введите фамилию для поиска записи: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+", encoding='utf-8') 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Найденная информация:", end = " ") 
            model.print_new(line) 
            found = True 
            break 
    if found == False: 
        print( "Данный контакт недоступен в телефонной книге", searchname)
    
# Ввод фамилии
def input_firstname(): 
    first = input( "Введите фамилию: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname  
 
# Ввод имени
def input_lastname(): 
    last = input( "Введите имя: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname   
 
# Ввод телефона и эл.адреса
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    
    while True:
        phoneNum = input( "Введите номер телефона: ")
        if len(phoneNum) == 11:
            break
        else:
            print('Номер указан неверно. Попробуйте еще раз')
    emailID = input( "Введите E-mail адрес: ")
    contactDetails =(firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "\n") 
    myfile = open(filename, "a", encoding='utf-8') 
    myfile.write(contactDetails) 
    model.print_new(f'Контакт: {contactDetails}был успешно сохранен!')

# удаление информации        
# def delcontact(): 
#     delname = input("Введите фамилию для удаления записи: ") 
#     with open (filename, 'w', encoding='utf-8') as myfile:
#         myfile.readlines()
#         for line in myfile:
#             if delname != line:
#                 myfile.write(line)
#                 print (line)
#     return myfile