from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base

class Journal(Base):
    __tablename__ = 'journals'
    
    id = Column(Integer, primary_key=True)
    entry = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    def __repr__(self):
        return f"Journal(id={self.id}, entry={self.entry[:20]}...)"