from random import *
from time import sleep
import sys
board = list(range(1,10))
def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)
# вводный текст
welcome_text = ('Здавствуйте!!! Я приветствую Вас!!!\n''Начинаем игру "Крестики-нолики"\n')
for c in welcome_text: 
    print (c, end = '')
    sys.stdout.flush() 
    sleep(0.09)
# ввод имен игроков и кто будет ходить первым
name1 = input('Введите имя первого игрока: ' )
name2 = input ('Введите имя второго игрока: ')
print (f"Здравствуйте {name1} и {name2} !!!\n")
print ('Сейчас определим ход первого игрока.\n')
i = randint(1,2)
if i == 1:
    first = name1
    two = name2
else:
    first = name2
    two = name1
print (f"Поздравляю {first} ходит первым!!!\n")
main(board)