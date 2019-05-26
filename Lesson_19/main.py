from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route("/")
def index():


    return render_template("index.html", user=user)


@app.route("/gethandler", methods=["GET"])
def login():
    secret_number = request.cookies.get("secret_number")

    if secret_number:

    name = request.form.get("user-name")
    email = request.form.get("user-email")

    user = User(name=name, email=email)
    user.create()

    response = make_response(redirect(url_for('index')))
    response.set_cookie("email", email)

    return response

@app.route("/posthandler", methods=["POST"])
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie("email", expires=0)

    return response

if __name__ == '__main__':
    app.run()