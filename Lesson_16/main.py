from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year

    cities = ["Boston", "Vienna", "Paris", "Berlin", "Budapest"]

    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities)

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("Fakebook/index.html")

@app.route("/portfolio/boogle")
def boogle():
    return render_template("Boogle/index.html")

@app.route("/portfolio/hairsalon")
def hairsalon():
    return render_template("Bootstrap/index.html")


if __name__ == '__main__':
    app.run()