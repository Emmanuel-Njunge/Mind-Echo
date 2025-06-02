from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.sql import func
from . import Base

class UserMood(Base):
    __tablename__ = 'user_moods'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    mood_id = Column(Integer, ForeignKey('moods.id'))
    datetime = Column(DateTime, server_default=func.now())
    notes = Column(String)
    
    def __repr__(self):
        return f"UserMood(id={self.id}, user_id={self.user_id}, mood_id={self.mood_id})"