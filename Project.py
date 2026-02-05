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
    username = input("enter your username: ").strip()
    users = load_users()
    if not os.path.exists(users):
        print("user not registered")
        return
    activity = input("enter yur activity: ").strip()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open (LOG_FILE, "a") as file:
        file.write(f"{time} | {username} |{activity} \n")
    print("activity log")


def view_log():
    username = input("enter username to view log: ").strip()

    if not os.path.exists(LOG_FILE):
        print("No log found")
        return
    
    with open (LOG_FILE, "r") as file:
        for line in file:
            if f"| {username} |" in line:
                print(line.strip())
                