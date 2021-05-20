import os
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


# Characters.html


@app.route("/characters")
def characters():
    roles = mongo.db.roles.find().sort("character_role", -1)
    characters = list(mongo.db.characters.find())
    return render_template(
        "characters.html", roles=roles, characters=characters)


# search characters on characters.html


@app.route("/search")
def search():
    query = request.args.get("query")
    characters = list(mongo.db.characters.find({"$text": {"$search": query}}))
    return render_template("characters.html", characters=characters)


# Create a character on characters.html


@app.route("/create_character/<username>", methods=["GET", "POST"])
def create_character(username):
    if request.method == "POST":
        characters = {
            "character_role": request.form.get("character_role"),
            "character_name": request.form.get("character_name"),
            "character_description": request.form.get("character_description"),
            "character_bio": request.form.get("character_bio"),
            "character_skills": request.form.get("character_skills"),
            "created_by": session["user"]
        }
        mongo.db.characters.insert_one(characters)
        flash("Character created.")
        return redirect(url_for("characters"))

    roles = mongo.db.roles.find().sort("character_role", 1)
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("create_character.html",
                               roles=roles, username=username)


# Edit a character on characters.html


@app.route("/edit_character/<characters_id>", methods=["GET", "POST"])
def edit_character(characters_id):
    if session and session["user"]:
        if request.method == "POST":
            edit = {
                "character_role": request.form.get("character_role"),
                "character_name": request.form.get("character_name"),
                "character_description": request.form.get(
                    "character_description"),
                "character_bio": request.form.get("character_bio"),
                "character_skills": request.form.get("character_skills"),
                "created_by": session["user"]
            }
            mongo.db.characters.update({"_id": ObjectId(characters_id)}, edit)
            flash("Character edited.")
            return redirect(url_for("characters"))

        characters = mongo.db.characters.find_one(
            {"_id": ObjectId(characters_id)})

        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        roles = mongo.db.roles.find().sort("character_role", 1)
        return render_template("edit_character.html", roles=roles,
                               username=username, characters=characters)
    else:
        return redirect(url_for("index"))


# Delete a character on characters.html


@app.route("/delete_character/<characters_id>")
def delete_characters(characters_id):
    if session and session["user"]:
        mongo.db.characters.remove({"_id": ObjectId(characters_id)})
        flash("Character deleted")
        return redirect(url_for("characters"))
    else:
        return redirect(url_for("index"))


# View character roles on roles.html


@app.route("/roles")
def roles():
    if session and session["user"] == "admin":
        roles = list(mongo.db.roles.find().sort("character_role", 1))
        return render_template("roles.html", roles=roles)
    else:
        return redirect(url_for("index"))


# Delete a character role on edit_role.html


@app.route("/delete_role/<role_id>")
def delete_role(role_id):
    if session and session["user"] == "admin":
        mongo.db.roles.remove({"_id": ObjectId(role_id)})
        flash("Role deleted")
        return redirect(url_for("roles"))
    else:
        return redirect(url_for("index"))


# Edit a character role on edit_role.html


@app.route("/edit_role/<role_id>", methods=["GET", "POST"])
def edit_role(role_id):
    if session and session["user"] == "admin":
        if request.method == "POST":
            submit = {
                "character_role": request.form.get("character_role")
            }
            mongo.db.roles.update({"_id": ObjectId(role_id)}, submit)
            flash("Role Updated!")
            return redirect(url_for("roles"))

        role = mongo.db.roles.find_one({"_id": ObjectId(role_id)})
        return render_template("edit_role.html", role=role)
    else:
        return redirect(url_for("index"))


# Add a character role on add_role.html


@app.route("/add_role", methods=["GET", "POST"])
def add_role():
    if session and session["user"] == "admin":
        if request.method == "POST":
            existing_role = mongo.db.roles.find_one(
                {"character_role": request.form.get("character_role").lower()})

            if existing_role:
                flash("Role already exists")
                return redirect(url_for("add_role"))

            role = {
                "character_role": request.form.get("character_role").lower()
            }

            mongo.db.roles.insert_one(role)
            flash("New Role created")
            return redirect(url_for("roles"))

        return render_template("add_role.html")
    else:
        return redirect(url_for("index"))


# Login Page


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check username
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username").capitalize()))
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


# Log out


@app.route("/logout")
def logout():
    flash("You've been logged out.")
    session.pop("user")
    return redirect(url_for("login"))


# Index Page


@app.route("/")
def index():
    return render_template("index.html")


# Contact Page


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Profile Page


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get active session username from db
    characters = list(mongo.db.characters.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, characters=characters)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
