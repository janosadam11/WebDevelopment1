import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))

class Guess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guesses = db.Column(db.String, unique=True)