# importing os and flask class and render template for HTML rendering
import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# creating an instance of the class and storing it in a variable called app
# the first argument of the Flask class, is name of application's module
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# app.route decorator wraps index function
@app.route("/")
def index():
    # render HTML file in templates folder
    return render_template("index.html")


@app.route("/about")
def about():
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have recieved your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # only debug=True when in Producton of software
        debug=True)
