import random
from os import system, name
from ast import literal_eval


with open('menu_unpicked.txt', 'r') as f:
    count = 0
    for line in f:
        if count == 0:
            main_dish = f.readlines()
            main_dish = literal_eval(main_dish)
    #main_dish = f.readline(0)
    #print(main_dish)
    #main_dish = literal_eval(main_dish)
        elif count == 1:
            breakfast = f.read()
            breakfast = literal_eval(breakfast)

def pick_a_dish():
    print('Here are your choices:')
    print(main_dish)
    picked_dish = random.choice(list(main_dish))
    print('You should cook: ' + picked_dish)
    
# define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for linux/mac
    else:
        _ = system('clear')

clear()
print('Hello to the dish selector!\n'
    + 'What do you want to do?\n'
    + '[1 - pick a main meal, 2 - exit]')

while True:
    
    decision = input().lower()

    if decision == '1':
        pick_a_dish()
    
    elif decision == '2':
        break
        


