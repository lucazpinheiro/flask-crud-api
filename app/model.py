from flask_sqlalchemy import SQLAlchemy

# init db
db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

