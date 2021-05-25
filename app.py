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


# View characters.html


@app.route("/characters")
def characters():
    roles = mongo.db.roles.find().sort("character_role")
    characters = list(mongo.db.characters.find().sort("_id", -1))
    return render_template(
        "characters.html", roles=roles, characters=characters)


# Search characters on characters.html


@app.route("/search")
def search():
    query = request.args.get("query")
    characters = list(mongo.db.characters.find({"$text": {"$search": query}}))
    return render_template("characters.html", characters=characters)


# Create a character on create_character.html


@app.route("/create_character", methods=["GET", "POST"])
def create_character():
    """
    1.  Check if user exists, then render create_character.html.
    2.  Match user enteries on a form to db key's (See 'characters' variable).
    3.  Update db roles and characters collections.
    """
    if session and session["user"]:
        if request.method == "POST":
            characters = {
                "character_role": request.form.get("character_role"),
                "character_name": request.form.get("character_name"),
                "character_description": request.form.get(
                    "character_description"),
                "character_bio": request.form.get("character_bio"),
                "character_skills": request.form.get("character_skills"),
                "created_by": session["user"]
            }
            mongo.db.characters.insert_one(characters)
            flash("Character created.")
            return redirect(url_for("characters"))

        roles = mongo.db.roles.find().sort("character_role")

        if session["user"]:
            return render_template("create_character.html",
                                   roles=roles)

    else:
        return redirect(url_for("index"))


# Edit a character on edit_character.html


@app.route("/edit_character/<characters_id>", methods=["GET", "POST"])
def edit_character(characters_id):
    """
    1.  Check if user exists, then render edit_character.html.
    2.  Match user enteries on a form to db key's (See 'edit' variable).
    3.  Update db roles and characters collections.
    """
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

        username = session["user"]

        roles = mongo.db.roles.find().sort("character_role")
        return render_template("edit_character.html", roles=roles,
                               username=username, characters=characters)
    else:
        return redirect(url_for("index"))


# Delete a character on characters.html


@app.route("/delete_character/<characters_id>")
def delete_character(characters_id):
    """
    1.  Check if user exists.
    2.  Delete intended character using selection's ID from db.
    """
    if session and session["user"]:
        mongo.db.characters.remove({"_id": ObjectId(characters_id)})
        flash("Character deleted")
        return redirect(url_for("characters"))
    else:
        return redirect(url_for("index"))


# View character roles on roles.html


@app.route("/roles")
def roles():
    """
    1.  Check if user is Admin.
        (Roles are only available to Admin.)
    2.  List Roles in alphabetical order.
    """
    if session and session["user"] == "admin":
        roles = list(mongo.db.roles.find().sort("character_role"))
        return render_template("roles.html", roles=roles)
    else:
        return redirect(url_for("index"))


# Delete a character role on edit_role.html


@app.route("/delete_role/<role_id>")
def delete_role(role_id):
    """
    1.  Check if user is Admin.
        (Role deletions are only available to Admin.)
    2.  Get ID of role to be deleted.
    3.  Remove ID of role from DB.
    """
    if session and session["user"] == "admin":
        mongo.db.roles.remove({"_id": ObjectId(role_id)})
        flash("Role deleted")
        return redirect(url_for("roles"))
    else:
        return redirect(url_for("index"))


# Edit a character role on edit_role.html


@app.route("/edit_role/<role_id>", methods=["GET", "POST"])
def edit_role(role_id):
    """
    1.  Check if user is Admin.
        (Role edits are only available to Admin.)
    2.  Get ID of role to be edited, and render edit_role.html
    3.  Update db using the role id and the 'character's role' key.
    """
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
    """
    1.  Check if user is Admin.
        (Role additions are only available to Admin.)
    2.  Check if new role already exists in DB. If yes, Flash and redirect.
    3.  If new role is unique insert it into the roles collection in db.
    """
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


# LOGIN


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    1.  Check user entry against db to verify username and password.
    2.  Return identical messages whether username or password are incorrect
        in case of brute force attack, and return to login.html.
    3.  On success welcome user and render profile page.
    """
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
                    "profile"))
            else:
                # Wrong Passowrd
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Wrong Username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    1.  Check existing usernames in db against user entry.
    2.  Store unique usernames in db, and hash passwords.
    3.  Assign successful username entry to session cookie,
        which is needed to render profile.html.
    """
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


# LOG OUT


@app.route("/logout")
def logout():
    flash("You've been logged out.")
    session.pop("user")
    return redirect(url_for("login"))


# INDEX


@app.route("/")
def index():
    return render_template("index.html")


# CONTACT


@app.route("/contact")
def contact():
    return render_template("contact.html")


# PROFILE


@app.route("/profile", methods=["GET", "POST"])
def profile():
    """
    1.  Check if user exists before rendering profile page.
    2.  The character list is arranged in order of most recently added.
    3.  The username is also used on profile.html greeting.
    """
    if session and session["user"]:
        characters = list(mongo.db.characters.find().sort("_id", -1))
        username = session["user"]
        return render_template(
                "profile.html", username=username, characters=characters)
    else:
        return redirect(url_for("index"))


# ERROR HANDLER


@app.errorhandler(404)
def page_not_found(e):
    """ Returns a 404.html on 404 errors """

    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
