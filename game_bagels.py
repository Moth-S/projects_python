from random import randint

def get_three_digits_num ():
    num=randint(100,999)
    return num

def Get_massage(user_num):
    if user_num==secret_num:
        return 'Yoy got it!'
    
    mess=[]
    for i in range(len(user_num)):
        if user_num[i]==secret_num[i]:
            mess.append('Fermi')
        elif user_num[i] in secret_num:
            mess.append('Pico')
    if len(mess)==0:
        return 'Bagels'
    else: 
        mess.sort()
        return ' '.join(mess)


print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
 Pico       One digit is correct but in the wrong position.
 Fermi      One digit is correct and in the right position.
 Bagels     No digit is correct.
I have thought up a number.
26 Проект 1. Бейглз
 You have 10 guesses to get it.
''')
agree='y'
while agree:
    secret_num=str(get_three_digits_num())
    for i in range(10):
        print(f'Guess #{i+1}')
        n=input()
        get_mess=Get_massage(n)
        if get_mess!='Yoy got it!':
            print(get_mess)
        else:
            print(get_mess)
            break
    print(secret_num)
    repeat_game=input('Do you want to play again? (y or n)')
    if repeat_game=='n':
        print('goodbye')
        break
