import sqlite3

dishName = input('Dish name: ')
popularity = int(input('Popularity: '))

conn = sqlite3.connect('dishes.db')
with conn:
    c = conn.cursor()
    c.execute("INSERT INTO MAIN_COURSE ('dish_name', popularity) VALUES ('%s', '%s')" %(dishName, popularity))