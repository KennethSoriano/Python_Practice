def login(database, username, password):
    if username in database and password == database[username]:
        print(f"\nWelcome back {username}!")
        return username
    elif username in database and password != database[username]:
        print("\nIncorrect password for admin.")
        return ""
    else:
        print("\nUsernam not found. Please register first.")
        return ""

def register(database, username):
    if username in database:
        print("\nUsername already registered.")
        return ""
    else: 
        print(f"\nUsername {username} registered")
        return username