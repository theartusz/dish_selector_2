import random
from os import system, name
from ast import literal_eval


with open('menu_unpicked.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
        if count == 1:
            main_meal = literal_eval(line)
        elif count == 2:
            breakfast = literal_eval(line)
        elif count == 3:
            salat = literal_eval(line)

def pick_main_meal(dish_type):
    print('Here are your choices:')
    print(dish_type)
    picked_dish = random.choice(list(dish_type))
    print('You should cook: ' + picked_dish)
    return True
    
    
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
    + '[1 - pick a main meal, 2 - salat, 3 - breakfast, exit]')

while True:
    
    decision = input().lower()

    if decision == '1':
        pick_main_meal(main_meal)
    
    elif decision == 'exit':
        break
        


