from app import db
import re

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        }
        return dict

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        }
        return dict

class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(100))
    customer = db.Column(db.String(100))
    film = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'owner': self.owner,
        'customer': self.customer,
        'film': self.film
        }
        return dict

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.String(100))
    year = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        'duration': self.duration,
        'year': self.year
        }
        return dict