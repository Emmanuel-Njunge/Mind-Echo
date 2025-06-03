from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Mood(Base):
    __tablename__ = 'moods'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    
    
    affirmations = relationship("Affirmation", backref="mood")
    user_moods = relationship("UserMood", back_populates="mood")

    
    def __repr__(self):
        return f"Mood(id={self.id}, name={self.name})"