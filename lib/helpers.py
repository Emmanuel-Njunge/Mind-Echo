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
    print(f"\nUser '{name}' created! Welcome aboard, emotionally available coder! 💻✨")
    print(random.choice([
        "Your commit history is beautiful today!",
        "We added you to the database of awesome people!",
        "User initialized with 100% happiness potential!"
    ]))
def view_user_history():
    user_id = input("Enter user ID: ")
    user = session.get(User, user_id)
    if not user:
        print("❌ User not found!")
        return

    print(f"\n=== {user.name}'s Mental Health Log ===")

    print("\n📝 Journals:")
    if user.journals:
        for journal in user.journals:
            print(f"- {journal.entry[:50]}...")
    else:
        print("No journal entries.")

    print("\n😊 Mood History:")
    if user.user_moods:
        for um in user.user_moods:
            mood_name = um.mood.name if um.mood and um.mood.name else "Unknown Mood"
            notes = um.notes if um.notes else "(no notes)"
            print(f"- Felt {mood_name}: '{notes}'")
    else:
        print("No moods logged.")

    print("\n💖 Affirmations Received:")
    moods = {um.mood_id for um in user.user_moods}
    if moods:
        for mood_id in moods:
            mood = session.get(Mood, mood_id)
            affirmations = session.query(Affirmation).filter_by(mood_id=mood_id).all()
            print(f"For mood '{mood.name}':")
            for affirmation in affirmations:
                print(f"- {affirmation.text}")
    else:
        print("No affirmations found.")


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