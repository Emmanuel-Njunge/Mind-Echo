from helpers import (
    exit_program,
    list_users,
    create_user,
    list_moods,
    create_mood,
    list_affirmations,
    create_affirmation,
    list_journals,
    create_journal,
    list_user_moods,
    create_user_mood,
    get_random_affirmation
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_users()
        elif choice == "2":
            create_user()
        elif choice == "3":
            list_moods()
        elif choice == "4":
            create_mood()
        elif choice == "5":
            list_affirmations()
        elif choice == "6":
            create_affirmation()
        elif choice == "7":
            list_journals()
        elif choice == "8":
            create_journal()
        elif choice == "9":
            list_user_moods()
        elif choice == "10":
            create_user_mood()
        elif choice == "11":
            get_random_affirmation()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all users")
    print("2. Create a new user")
    print("3. List all moods")
    print("4. Create a new mood")
    print("5. List all affirmations")
    print("6. Create a new affirmation")
    print("7. List all journals")
    print("8. Create a new journal")
    print("9. List all user moods")
    print("10. Create a new user mood")
    print("11. Get random affirmation for mood")

if __name__ == "__main__":
    main()