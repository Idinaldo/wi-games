from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Game(db.Model):

    __tablename__ = "game"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    developer = db.Column(db.String(80))


    def __init__(self, name, developer):
        self.name = name
        self.developer = developer

    def __repr__(self):
        return f"{self.developer}:{self.name}"
    
