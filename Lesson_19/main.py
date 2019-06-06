import random
from flask import Flask, render_template, request, make_response
from Lesson_19.models import Guess, db

app = Flask(__name__)
db.create_all()


@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")
    user = db.query(Guess).filter(Guess.guesses).all()
    print(user.Guess.guesses)



    response = make_response(render_template("index.html"))
    if not secret_number:
        user = db.query(Guess).filter_by(Guess.guesses).first()
        new_secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret))
        if user:
            print(user.Guess.guesses)

    return response


@app.route("/posthandler", methods=["POST"])
def posthandler():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        message = "Congratulations! The secret number is: {0}".format(str(secret_number))
        response = make_response(render_template("guess.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))
        return response
    elif guess > secret_number:
        request.form.get("guess")
        actual_guess = Guess(guesses=guess)
        db.add(actual_guess)
        db.commit()
        message = "Too big, guess smaller!"
        return render_template("guess.html", message=message)
    elif guess < secret_number:
        request.form.get("guess")
        actual_guess = Guess(guesses=guess)
        db.add(actual_guess)
        db.commit()
        message = "Too small, guess bigger!"
        return render_template("guess.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)