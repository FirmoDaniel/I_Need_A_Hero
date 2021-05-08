import os
import json
from flask import (
    Flask, render_template, request, flash,
    redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
    # list added below to run two for loops on one page(info.html)
    infos = list(mongo.db.info.find())
    return render_template("info.html", infos=infos)


# search function on browse page


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    infos = list(mongo.db.info.find({"$text": {"$search": query}}))
    return render_template("info.html", infos=infos)


# Log out
@app.route("/logout")
def logout():
    flash("You've been logged out. #SadTimes! Come back soon")
    session.pop("user")
    return redirect(url_for("login"))


# Create  Page


@app.route("/create/<username>", methods=["GET", "POST"])
def create(username):
    # Copied from Profile.html set up.
    if request.method == "POST":
        infos = {
            "characters_role": request.form.get("characters_role"),
            "infos_name": request.form.get("infos_name"),
            "infos_description": request.form.get("infos_description"),
            "created_by": session["user"]
        }
        mongo.db.info.insert_one(infos)
        flash("Clever Hooman! Character created.")
        return redirect(url_for("get_info"))

    characters = mongo.db.characters.find().sort("characters_role", 1)
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("create.html", username=username, 
            characters=characters)


# edit button/function on create.html


@app.route("/edit_info/<info_id>", methods=["GET", "POST"])
def edit_info(info_id):
    if request.method == "POST":
        edit = {
            "characters_role": request.form.get("characters_role"),
            "infos_name": request.form.get("infos_name"),
            "infos_description": request.form.get("infos_description"),
            "infos_bio": request.form.get("infos_bio"),
            "infos_skills": request.form.get("infos_skills"),
            "created_by": session["user"]
        }
        mongo.db.info.update({"_id": ObjectId(info_id)}, edit)
        flash("Clever Hooman! Character Edited.")
        return redirect(url_for("get_info"))

    info = mongo.db.info.find_one({"_id": ObjectId(info_id)})

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    characters = mongo.db.characters.find().sort("characters_role", 1)
    return render_template("edit_info.html", info=info, 
        username=username, characters=characters)


# delete button/function on create.html


@app.route("/delete_info/<info_id>")
def delete_info(info_id):
    mongo.db.info.remove({"_id": ObjectId(info_id)})
    flash("Fearless Hooman! Character Obliterated")
    return redirect(url_for("get_info"))


# Delete Role Page
@app.route("/delete_role/<character_id>")
def delete_role(character_id):
    mongo.db.characters.remove({"_id": ObjectId(character_id)})
    flash("Role deleted")
    return redirect(url_for("browse"))


# Edit Character Role  Page


@app.route("/edit_role/<character_id>", methods=["GET", "POST"])
def edit_role(character_id):
    if request.method == "POST":
        submit = {
            "characters_role": request.form.get("characters_role")
        }
        mongo.db.characters.update({"_id": ObjectId(character_id)}, submit)
        flash("Role Updated!")
        return redirect(url_for("browse"))

    character = mongo.db.characters.find_one({"_id": ObjectId(character_id)})
    return render_template("edit_role.html", character=character)


# Add Character Role  Page


@app.route("/add_role", methods=["GET", "POST"])
def add_role():
    if request.method == "POST":
        character = { 
            "characters_role": request.form.get("characters_role")
        }
        mongo.db.characters.insert_one(character)
        flash("New Role created")
        return redirect(url_for("browse"))

    return render_template("add_role.html")


# Browse  Page


@app.route("/browse")
def browse():
    characters = mongo.db.characters.find().sort("characters_role", 1)
    return render_template("browse.html", characters=characters)


# Profile  Page


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get active session username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Login Page


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            # check username
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Wrong Passowrd
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Wrong Username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Register Page


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
           flash("Username already exists")
           return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Routing for main pages


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/examples")
def examples():
    data = []
    with open("data/characters.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        "examples.html", page_title="Examples", characters=data)


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
