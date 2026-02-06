from datetime import datetime
import os

USERS_FILE = "users.txt"
LOG_FILE = "activity.log"
BACKUP_FILE = "activity_backup.log"
SUMMARY_FILE = "summary.txt"


def backup_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as src:
            data = src.read()
        with open(BACKUP_FILE, "w") as dst:
            dst.write(data)


def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w"):
            pass

    with open(USERS_FILE, "r") as file:
        return [line.strip() for line in file]


def register_user():
    username = input("Enter username: ").strip()

    users = load_users()
    if username in users:
        print("User already exists")
        return

    with open(USERS_FILE, "a") as file:
        file.write(username + "\n")

    print("User registered successfully")


def log_activity():
    username = input("Enter username: ").strip()
    users = load_users()

    if username not in users:
        print("User not registered")
        return

    activity = input("Enter activity: ").strip()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{time} | {username} | {activity}\n")

    print("Activity logged")


def view_logs():
    username = input("Enter username to view logs: ").strip()

    if not os.path.exists(LOG_FILE):
        print("No logs found")
        return

    with open(LOG_FILE, "r") as file:
        for line in file:
            if f"| {username} |" in line:
                print(line.strip())


def generate_summary():
    count = 0

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            for _ in file:
                count += 1

    with open(SUMMARY_FILE, "w") as file:
        file.write(f"Total activities: {count}")

    print("Summary created")


def menu():
    print("\n1. Register User")
    print("2. Log Activity")
    print("3. View User Logs")
    print("4. Generate Summary")
    print("5. Exit")


def main():
    backup_log()

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            log_activity()
        elif choice == "3":
            view_logs()
        elif choice == "4":
            generate_summary()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option")


main() 
