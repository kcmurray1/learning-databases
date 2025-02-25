from flask import Blueprint, render_template, request, redirect

views = Blueprint('views', __name__, template_folder="../app/frontend/templates")

@views.route("/")
def index():
    return render_template("index.html")