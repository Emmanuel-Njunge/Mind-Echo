from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base

class Affirmation(Base):
    __tablename__ = 'affirmations'
    
    id = Column(Integer, primary_key=True)
    text = Column(String)
    mood_id = Column(Integer, ForeignKey('moods.id'))
    
    def __repr__(self):
        return f"Affirmation(id={self.id}, text={self.text[:20]}...)"