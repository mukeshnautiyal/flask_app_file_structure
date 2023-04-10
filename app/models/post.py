from app.extensions import db
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.utils.common import today
from app.models.user import User
#from flask_appbuilder import Model



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship("User")
    created_on = Column(db.DateTime, default=today, nullable=False)
    updated_on = Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Post "{self.title}">'
        
        