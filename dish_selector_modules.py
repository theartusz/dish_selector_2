import random
import sqlite3
import pandas
from os import system
from os import name

def read_menu(table):
    conn = sqlite3.connect('dishes.db')

    with open('schema.sql') as f:
        conn.executescript(f.read())
        
    query = 'SELECT * FROM ' + table
    menu = pandas.read_sql(query,conn)
    # read from _orig table if all dishes were used
    if len(menu.index) == 0:
        query = 'SELECT * FROM ' + table + '_orig'
        menu = pandas.read_sql(query,conn)
    conn.close()
    return menu

def pick_meal(dish_type_df):
    menu_len = len(dish_type_df.index)
    meal_choice = random.randint(0, menu_len - 1)
    meal = dish_type_df.iloc[[meal_choice], [1]].to_string(header=False, index=False).strip()
    return meal

def add_meal():
    dish_name = input('Dish name: ').lower()
    popularity = int(input('Popularity: '))
    dish_type = input('Disch Type [main\\salat]: ').lower()
    if dish_type == 'main': 
        dish_type = 'main_course'
    
    conn = sqlite3.connect('dishes.db')
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM " + dish_type + "_orig WHERE dish_name = '%s'" % (dish_name))
        if len(c.fetchall()) > 0:
            print('Record already exists in database.\n'
                + 'Do you want to update it?')
            update_record = input('[y/n]: ').lower()
            if update_record == 'y':
                c.execute("UPDATE " + dish_type + "_orig SET popularity = '%s' WHERE dish_name = '%s'" % (popularity, dish_name))
        else: c.execute("INSERT INTO " + dish_type + "_orig (dish_name, popularity) VALUES ('%s', '%s')" % (dish_name, popularity))
    
# define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for linux/mac
    else:
        _ = system('clear')

"""""""""""""""""""""""""""""""""""""""""""""""""""
Program start
"""""""""""""""""""""""""""""""""""""""""""""""""""

clear()
main_course_df = read_menu('main_course')
salat_df = read_menu('salat')

#print('Hello to the dish selector!')
#
##while True:
#print('\nWhat do you want to do?\n'
#    + '[1 - pick a main course, 2 - pick salat, 4 - options, 5 - add meal, exit]')

#decision = input().lower()
#decision = 'exit'

#if decision == '1':
#    main_course_df = pick_meal(main_course_df)
#
#elif decision == '2':
#    salat_df = pick_meal(salat_df)
#
#elif decision == '4':
#    print(main_course_df[['dish_name', 'popularity']])
#    print(salat_df[['dish_name', 'popularity']])
#
#elif decision == '5':
#    add_meal()
#
#elif decision == 'exit':
#    conn = sqlite3.connect('dishes.db')
#    with conn:
#        main_course_df.to_sql('main_course', conn, if_exists='replace', index=False)
#        salat_df.to_sql('salat', conn, None, 'replace', False)