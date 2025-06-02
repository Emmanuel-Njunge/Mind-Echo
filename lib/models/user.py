from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
 
    journals = relationship("Journal", backref="user")
    user_moods = relationship("UserMood", backref="user")
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"