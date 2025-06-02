from models import session
from models.user import User
from models.mood import Mood
from models.affirmation import Affirmation
from models.journal import Journal
from models.user_mood import UserMood
from faker import Faker
import random

fake = Faker()

def seed_data():
    #Clear existing data
    session.query(User).delete()
    session.query(Mood).delete()
    session.query(Affirmation).delete()
    session.query(Journal).delete()
    session.query(UserMood).delete()

    # Create users
    users = []
    for _ in range(5):
        user = User(name=fake.name())
        users.append(user)
        session.add(user)
    
    # Create moods
    mood_names = ["Happy", "Sad", "Anxious", "Excited", "Calm"]
    moods = []
    for name in mood_names:
        mood = Mood(name=name, description=f"This is when you feel {name.lower()}")
        moods.append(mood)
        session.add(mood)
    
    # Create affirmations
    affirmation_data = {
        "Happy": [
            "You deserve happiness today!",
            "Joy flows through you easily.",
            "You are a magnet for positive experiences."
        ],
        "Sad": [
            "This feeling is temporary.",
            "You are stronger than you think.",
            "It's okay to not be okay."
        ],
        "Anxious": [
            "You are safe in this moment.",
            "Breathe deeply and release tension.",
            "This too shall pass."
        ],
        "Excited": [
            "Great things are coming your way!",
            "Your enthusiasm is contagious.",
            "The universe is conspiring in your favor."
        ],
        "Calm": [
            "Peace begins with you.",
            "You are centered and grounded.",
            "All is well in your world."
        ]
    }
    
    for mood in moods:
        for text in affirmation_data.get(mood.name, []):
            affirmation = Affirmation(text=text, mood_id=mood.id)
            session.add(affirmation)
    
    # Create journals
    for user in users:
        for _ in range(2):
            journal = Journal(
                entry=fake.paragraph(),
                user_id=user.id
            )
            session.add(journal)
    
    # Create user moods
    for user in users:
        for _ in range(3):
            user_mood = UserMood(
                user_id=user.id,
                mood_id=random.choice(moods).id,
                notes=fake.sentence()
            )
            session.add(user_mood)
    
    session.commit()
    print("Database seeded!")

if __name__ == "__main__":
    seed_data()