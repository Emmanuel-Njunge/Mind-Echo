# MindEcho CLI

MindEcho CLI is a command-line application designed to support mental wellness through positive affirmations. Users interact by selecting their mood, and the system provides uplifting affirmations tailored to their emotional state. The application stores mood history and journal entries in a structured SQLAlchemy ORM database, allowing users to track their personal reflections and emotional patterns over time.

###
“MindEcho — your emotionally intelligent terminal buddy, powered by Python and powered by your feelings. It logs your moods better than git logs commits — and won’t crash when you do.”

## Features

- Manage users and their moods
- Create and view affirmations for different moods
- Journal entries for users
- Track user moods over time
- Get random affirmations based on mood

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pipenv install
   pipenv shell
3.Initialize the database:
   python lib/init_db.py

4. Seed with sample data:
   python lib/seed.py

5.Run the CLI:
   python lib/cli.py


File Structure:
1.lib/cli.py: Main CLI interface

2.lib/helpers.py: Helper functions for database operations

3.lib/models/: Database models (one file per model)

4.lib/init_db.py: Database initialization

5.lib/seed.py: Database seeding with sample data



## Key Features

1. **Simple CLI Interface**: Easy-to-use menu system
2. **Database Relationships**:
   - One-to-many: User has many Journals
   - One-to-many: Mood has many Affirmations
   - Many-to-many: Users can have many Moods through UserMood
3. **Random Affirmations**: The `get_random_affirmation` function provides random affirmations based on mood
4. **Beginner-Friendly**: Simple Python code that's easy to understand and explain

This implementation meets all the project requirements while keeping the code simple enough for someone with 2 weeks of Python experience to understand and explain. The CLI is straightforward, the database relationships are properly modeled, and the code follows good practices without being overly complex.

Would you like me to explain any part of this implementation in more detail?

