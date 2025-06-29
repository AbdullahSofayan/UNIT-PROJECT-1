from utils.file_handler import load_json, save_json

USER_FILE = "users.json"

def load_users():
    return load_json(USER_FILE)

def save_users(users):
    save_json(USER_FILE, users)

def user_exists(username):
    return any(u["username"] == username for u in load_users())

def register_user():
    role = input("Role (admin/customer): ").lower()
    if role not in ["admin", "customer"]:
        print("Invalid role.")
        return None

    username = input("Username: ")
    if user_exists(username):
        print("Username exists.")
        return None

    password = input("Password: ")
    name = input("Name: ")
    email = input("Email: ")

    user = {"username": username, "password": password, "name": name, "email": email, "role": role}

    users = load_users()
    users.append(user)
    save_users(users)
    return user

def login_user():
    username = input("Username: ")
    password = input("Password: ")
    for user in load_users():
        if user["username"] == username and user["password"] == password:
            return user
    print("Login failed.")
    return None