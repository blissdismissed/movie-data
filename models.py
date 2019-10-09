from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    favorite = db.Column(db.String(120), index=True, unique=True) #will probably need to separate this into it's own table with id as the foreign key?

    def __repr__(self):
        return '<User {}>'.format(self.username)

