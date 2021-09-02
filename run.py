# importing os and flask class and render template for HTML rendering
import os
from flask import Flask, render_template

# creating an instance of the class and storing it in a variable called app
# the first argument of the Flask class, is name of application's module
app = Flask(__name__)


# app.route decorator wraps index function
@app.route("/")
def index():
    # render HTML file in templates folder
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # only debug=True when in Producton of software
        debug=True)
