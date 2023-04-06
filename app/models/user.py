from app.extensions import db

 


class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    age = db.Column(db.Integer)
    bio = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Student {self.firstname}>'