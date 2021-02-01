from flask import Flask, render_template
import pandas
import sqlite3
import random
import dish_selector_modules as ds

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main_course')
def select_main_course():
    main_course_df = ds.read_menu('main_course')
    meal_choice = ds.pick_meal(main_course_df)
    return render_template('main_course.html', meal_choice=meal_choice)