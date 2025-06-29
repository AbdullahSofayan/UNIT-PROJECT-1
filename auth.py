from utils.file_handler import load_json, save_json
import re
USER_FILE = "users.json"

def load_users():
    return load_json(USER_FILE)

def save_users(users):
    save_json(USER_FILE, users)

def user_exists(username):
    return any(u["username"] == username for u in load_users())

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def register_user():
    print("\n--- Register ---")
    role = input("Enter role (admin/customer): ").lower()
    if role != "admin" and role != "customer":
        print("Please enter either 'admin' or 'customer'.")
        return None

    username = input("Enter username: ")
    if user_exists(username):
        print("This username already exists. Try another.")
        return None

    password = input("Enter password: ")
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    if not is_valid_email(email):
        print("Invalid email format. Please try again.")
        return None

    new_user = {
        "username": username,
        "password": password,
        "name": name,
        "email": email,
        "role": role
    }

    users = load_users()
    users.append(new_user)
    save_users(users)
    return new_user

def login_user():
    while True:
        username = input("Username: ")
        if not user_exists(username):
            print("Username not Exist.\n")
            continue

        else:
            password = input("Password: ")
            for user in load_users():
                if user["username"] == username and user["password"] == password:
                    return user
            print("Login failed.")
            break
  
        