from app.extensions import db
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.utils.common import today
from app.models.user import User
from app.models.post import Post


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    answer = db.Column(db.Text)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship("User")
    post_id = Column(Integer, ForeignKey(Post.id), nullable=False)
    post = relationship("Post")
    created_on = Column(db.DateTime, default=today, nullable=False)
    updated_on = Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Question {self.content}>'