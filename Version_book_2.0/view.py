import controller
import model
import os


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

