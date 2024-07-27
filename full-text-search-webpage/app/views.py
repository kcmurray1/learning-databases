from flask import Blueprint, render_template, request, redirect
from app.database.database import BookDatabase
from threading import Lock

views = Blueprint('views', __name__,  template_folder="../app/frontend/templates")
database = BookDatabase("app/database/books_final.db")
db_lock = Lock()

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/about')
def about():
    database.reset()
    return render_template("about.html")

@views.route('/contact')
def contact():
    database.reset()
    return render_template("contact.html")

@views.route('/database')
def data():
    book_data = {"data": []}
    with db_lock, database as db:
        book_data["data"] = db.get_books()
    return book_data

@views.route('/database/filters')
def filters():
    filter_data = {"data": []}
    with db_lock, database as db:
        filter_data["data"] = db.get_categories()
    return filter_data 

@views.route('/database/filter')
def filtered():
    search_term = request.args.get("query")
    for value in request.args.values():
        print(value)
    return redirect("/")