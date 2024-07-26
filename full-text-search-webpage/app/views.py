from flask import Blueprint, render_template
from app.database.database import BookDatabase

views = Blueprint('views', __name__,  template_folder="../app/frontend/templates")

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/database')
def data():
    book_data = {"data": "undefined"}
    with BookDatabase("app/database/relational-books.db") as db:
        book_data["data"] = db.get_books()
    return book_data
