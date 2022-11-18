from tkinter import *  
from tkinter import messagebox  
  
def clicked():  
    messagebox.showinfo()
    
  
window = Tk()  
window.title("Добро пожаловать в телефонный справочник")  
window.geometry('250x550')  
lbl = Label(window, text="МЕНЮ СПРАВОЧНИКА")  
lbl.grid(column=0, row=0)  

a='Контакты телефонного справочника'
b=None
btn = Button(window, text="1. Показать все существующие контакты", command=clicked)  
btn.grid(column=0, row=200)
 

a='Введите ФИО'
b=None 
btn = Button(window, text="2. Добавить новый контакт", command=clicked)  
btn.grid(column=0, row=500) 


window.mainloop()



