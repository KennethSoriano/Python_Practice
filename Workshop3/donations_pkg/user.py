def login(database, username, password):
    database = { }
    username = ""
    password = ""
    if username in database and password == database[username]:
        print("\nWelcome back admin!")
        return username
    if username in database and password != database[username]:
        print("\nIncorrect password for admin.")
        return ""
    if username not in database:
        print("\nUser not found. Please register")
        return ""

def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else: 
        print("Username", username + " registered")