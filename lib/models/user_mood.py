from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import Base

class UserMood(Base):
    __tablename__ = 'user_moods'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    mood_id = Column(Integer, ForeignKey('moods.id'))
    datetime = Column(DateTime, server_default=func.now())
    notes = Column(String)
    
    # Add relationships
    user = relationship("User", back_populates="user_moods")
    mood = relationship("Mood", back_populates="user_moods")

    
    def __repr__(self):
        user_name = self.user.name if self.user else "Unknown User"
        mood_name = self.mood.name if self.mood else "Unknown Mood"
        return f"<UserMood(user='{user_name}', mood='{mood_name}', notes='{self.notes}')>"