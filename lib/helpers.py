from models import session
from models.user import User
from models.mood import Mood
from models.affirmation import Affirmation
from models.journal import Journal
from models.user_mood import UserMood
import random

def exit_program():
    print("Goodbye!")
    exit()

# User functions
def list_users():
    users = session.query(User).all()
    for user in users:
        print(user)

def create_user():
    name = input("Enter user name: ")
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User {name} created!")

# Mood functions
def list_moods():
    moods = session.query(Mood).all()
    for mood in moods:
        print(mood)

def create_mood():
    name = input("Enter mood name: ")
    description = input("Enter mood description: ")
    mood = Mood(name=name, description=description)
    session.add(mood)
    session.commit()
    print(f"Mood {name} created!")

# Affirmation functions
def list_affirmations():
    affirmations = session.query(Affirmation).all()
    for affirmation in affirmations:
        print(affirmation)

def create_affirmation():
    text = input("Enter affirmation text: ")
    mood_id = input("Enter mood ID: ")
    affirmation = Affirmation(text=text, mood_id=mood_id)
    session.add(affirmation)
    session.commit()
    print(f"Affirmation created!")

def get_random_affirmation():
    mood_id = input("Enter mood ID to get affirmation for: ")
    affirmations = session.query(Affirmation).filter_by(mood_id=mood_id).all()
    if affirmations:
        print(random.choice(affirmations).text)
    else:
        print("No affirmations found for this mood")
        
# Journal functions
def list_journals():
    journals = session.query(Journal).all()
    for journal in journals:
        print(journal)

def create_journal():
    entry = input("Enter journal entry: ")
    user_id = input("Enter user ID: ")
    journal = Journal(entry=entry, user_id=user_id)
    session.add(journal)
    session.commit()
    print(f"Journal entry created!")

# UserMood functions
def list_user_moods():
    user_moods = session.query(UserMood).all()
    for user_mood in user_moods:
        print(user_mood)

def create_user_mood():
    user_id = input("Enter user ID: ")
    mood_id = input("Enter mood ID: ")
    notes = input("Enter notes (optional): ")
    user_mood = UserMood(user_id=user_id, mood_id=mood_id, notes=notes)
    session.add(user_mood)
    session.commit()
    print(f"User mood created!")