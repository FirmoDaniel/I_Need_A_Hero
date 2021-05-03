import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


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
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
