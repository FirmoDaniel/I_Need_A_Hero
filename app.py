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

# Characters Page


@app.route("/get_info")
def get_info():
    # list added below to run two for loops on one page(characters.html)
    # info.html is tagged as 'Characters' on base template navbar.
    query = request.args.get("query")
    if query:
        infos = list(mongo.db.info.find(
            {"$text": {"$search": query}}).sort("_id", -1))
    else:
        infos = list(mongo.db.info.find().sort("_id", -1))
    characters = mongo.db.characters.find().sort("characters_role", 1)
    return render_template("info.html", infos=infos, characters=characters)


# search function on Characters Page


@app.route("/search", methods=["GET", "POST"])
def search():
    if session and session['user']:
        query = request.form.get("query")
        infos = list(mongo.db.info.find({"$text": {"$search": query}}))
        return render_template("info.html", infos=infos)
    else:
        return redirect(url_for('index'))


# edit button/function on Characters Page


@app.route("/edit_info/<info_id>", methods=["GET", "POST"])
def edit_info(info_id):
    if session and session['user']:
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
            flash("Character edited.")
            return redirect(url_for("get_info"))

        info = mongo.db.info.find_one({"_id": ObjectId(info_id)})

        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        characters = mongo.db.characters.find().sort("characters_role", 1)
        return render_template("edit_info.html", info=info,
                            username=username, characters=characters)
    else:
        return redirect(url_for('index'))


# delete button/function on Characters Page


@app.route("/delete_info/<info_id>")
def delete_info(info_id):
    if session and session['user']:
        mongo.db.info.remove({"_id": ObjectId(info_id)})
        flash("Character deleted")
        return redirect(url_for("get_info"))
    else:
        return redirect(url_for('index'))


# Roles  Page


@app.route("/roles")
def roles():
    if session and session['user']:
        characters = mongo.db.characters.find().sort("characters_role", 1)
        return render_template("roles.html", characters=characters)
    else:
        return redirect(url_for('index'))


# Delete Role Page


@app.route("/delete_role/<character_id>")
def delete_role(character_id):
    if session and session['user']:
        mongo.db.characters.remove({"_id": ObjectId(character_id)})
        flash("Role deleted")
        return redirect(url_for("roles"))
    else:
        return redirect(url_for('index'))


# Edit Character Role  Page


@app.route("/edit_role/<character_id>", methods=["GET", "POST"])
def edit_role(character_id):
    if session and session['user']:
        if request.method == "POST":
            existing_role = mongo.db.characters.find_one(
                {"characters_role": request.form.get("characters_role").lower()})

            if existing_role:
                flash("Role already exists")
                return redirect(url_for('roles'))

            submit = {
                "characters_role": request.form.get("characters_role")
            }
            mongo.db.characters.update({"_id": ObjectId(character_id)}, submit)
            flash("Role Updated!")
            return redirect(url_for("roles"))

        character = mongo.db.characters.find_one({"_id": ObjectId(character_id)})
        return render_template("edit_role.html", character=character)
    else:
        return redirect(url_for('index'))


# Add Character Role  Page


@app.route("/add_role", methods=["GET", "POST"])
def add_role():
    if session and session['user']:
        if request.method == "POST":
            existing_role = mongo.db.characters.find_one(
                {"characters_role": request.form.get("characters_role").lower()})

            if existing_role:
                flash("Role already exists")
                return redirect(url_for("add_role"))

            character = {
                "characters_role": request.form.get("characters_role").lower()
            }
            mongo.db.characters.insert_one(character)
            flash("New Role created")
            return redirect(url_for("roles"))
    else:
        return redirect(url_for('index'))


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


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, message recieved.".format(
            request.form.get("name").capitalize()))
    return render_template("contact.html")


# Profile  Page


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if session and session['user']:
        # get active session username from db
        infos = list(mongo.db.info.find())
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        if session["user"]:
            return render_template("profile.html", username=username, infos=infos)

        return redirect(url_for("login"))
    else:
        return redirect(url_for('index'))


# delete button/function on Profile Page


@app.route("/delete_info_profile/<info_id>")
def delete_info_profile(info_id):
    mongo.db.info.remove({"_id": ObjectId(info_id)})
    flash("Character deleted")
    return redirect(url_for("profile", username=session["user"]))


# Create character from profile page


@app.route("/create_character_from_profile/<username>", methods=["GET", "POST"])
def create_character_from_profile(username):
    if session and session['user']:
        if request.method == "POST":
            infos = {
                "characters_role": request.form.get("characters_role"),
                "infos_name": request.form.get("infos_name"),
                "infos_description": request.form.get("infos_description"),
                "infos_bio": request.form.get("infos_bio"),
                "infos_skills": request.form.get("infos_skills"),
                "created_by": session["user"]
            }
            mongo.db.info.insert_one(infos)
            flash("Character created.")
            return redirect(url_for("profile", username=session["user"]))

        characters = mongo.db.characters.find().sort("characters_role", 1)
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        if session["user"]:
            return render_template("create_character_from_profile.html", username=username,
                                characters=characters)
    else:
        return redirect(url_for('index'))


# edit button/function on profile Page


@app.route("/edit_info_from_profile/<info_id>", methods=["GET", "POST"])
def edit_info_from_profile(info_id):
    if session and session['user']:
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
            flash("Character edited.")
            return redirect(url_for("profile", username=session["user"]))

        info = mongo.db.info.find_one({"_id": ObjectId(info_id)})

        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        characters = mongo.db.characters.find().sort("characters_role", 1)
        return render_template("edit_info_from_profile.html", info=info,
                            username=username, characters=characters)
    else:
        return redirect(url_for('index'))


# Create Character Page


@app.route("/create_character", methods=["GET", "POST"])
def create_character():
    if session and session['user']:
        if request.method == "POST":
            infos = {
                "characters_role": request.form.get("characters_role"),
                "infos_name": request.form.get("infos_name"),
                "infos_description": request.form.get("infos_description"),
                "infos_bio": request.form.get("infos_bio"),
                "infos_skills": request.form.get("infos_skills"),
                "created_by": session["user"]
            }
            mongo.db.info.insert_one(infos)
            flash("Character created.")
            return redirect(url_for("get_info"))

            characters = mongo.db.characters.find().sort("characters_role", 1)

        return render_template("create_character.html", username=session['user'],
                               characters=characters)
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
