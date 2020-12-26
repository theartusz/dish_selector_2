import random
import sqlite3
from os import system, name

def add_meal():
    dish_name = input('Dish name: ')
    popularity = int(input('Popularity: '))

    conn = sqlite3.connect('dishes.db')
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM main_course WHERE dish_name = '%s'" % (dish_name))
        if len(c.fetchall()) > 0:
            print('Record already exists in database.\n'
                + 'Do you want to update it?')
            updateRecord = input('[y/n]: ')
            if updateRecord == 'y':
                c.execute("UPDATE main_course SET popularity = '%s' WHERE dish_name = '%s'" % (popularity, dish_name))
        else: c.execute("INSERT INTO main_course (dish_name, popularity) VALUES ('%s', '%s')" % (dish_name, popularity))
    
# define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for linux/mac
    else:
        _ = system('clear')

clear()
print('Hello to the dish selector!')

while True:
    print('\nWhat do you want to do?\n'
        + '[1 - pick a main meal, 2 - salat, 3 - breakfast, 4 - add meal, exit]')
    
    decision = input().lower()
    
    if decision == '4':
        add_meal()
    
    elif decision == 'exit':
        break
        


