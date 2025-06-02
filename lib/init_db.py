from models import Base, engine
from models.user import User
from models.mood import Mood
from models.affirmation import Affirmation
from models.journal import Journal
from models.user_mood import UserMood

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(engine)
    print("Database initialized!")

if __name__ == "__main__":
    init_db()