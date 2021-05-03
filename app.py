import os
import json
from flask import (
    Flask, render_template, request, flash,
    redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Routing for DB pages


@app.route("/get_info")
def get_info():
    infos = mongo.db.info.find()
    return render_template("info.html", infos=infos)


# Routing for main pages


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/examples")
def examples():
    data = []
    with open("data/characters.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("examples.html", page_title="Examples", characters=data)


@app.route("/examples/<character_name>")
def about_character(character_name):
    character = {}
    with open("data/characters.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == character_name:
                character = obj
    return render_template("characters.html", character=character)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, Message recieved".format(request.form.get("name")))
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
