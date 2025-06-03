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
    get_random_affirmation,
    view_user_history  
)

def exit_program():
    print("Peace out, code warrior! Keep your variables tight and your spirits high! 🚀")
    exit()

def menu():
    print("\n=== MAIN MENU ===")
    print("👤 USERS:         List(1) | Add(2)")
    print("😊 MOODS:         List(3) | Add(4)")
    print("💖 AFFIRMATIONS:  List(5) | Add(6) | Random(11)")
    print("📝 JOURNALS:      List(7) | Add(8)")
    print("🧠 HISTORY:       User Moods(9) | Add(10) | View(12)")  
    print("0. Exit")

def main():
    print(r"""
███╗   ███╗██╗███╗   ██╗██████╗ ███████╗ ██████╗██╗  ██╗ ██████╗ 
████╗ ████║██║████╗  ██║██╔══██╗██╔════╝██╔════╝██║  ██║██╔═══██╗
██╔████╔██║██║██╔██╗ ██║██║  ██║█████╗  ██║     ███████║██║   ██║
██║╚██╔╝██║██║██║╚██╗██║██║  ██║██╔══╝  ██║     ██╔══██║██║   ██║
██║ ╚═╝ ██║██║██║ ╚████║██████╔╝███████╗╚██████╗██║  ██║╚██████╔╝
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝
""")
    print("=== Welcome to MindEcho ===")
    print("The only therapist that:")
    print("- Runs on Python 🐍")
    print("- Never judges your life choices 🧘")
    print("- Charges 0 bugs/hour 🐞\n")

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
        elif choice == "12":
            view_user_history()
        else:
            print("\n🚨 Invalid choice! Try again.")
            print("Pro Tip: Numbers work better than feelings here.")
            print("(But in MindEcho, we validate ALL emotions! 💖)\n")
            print(r'''
    (╯°□°）╯︵ ┻━┻  
    That’s not even a valid option.
    Try something from 0 to 12!
''')

if __name__ == "__main__":
    main()
