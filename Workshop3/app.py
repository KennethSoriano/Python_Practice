# File Name: app.py
# About: This is an application that uses the donation package to process a users donations and account information



from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = { "admin": "password123"}
donations = [ ]
authorized_user = " "

while True:
    show_homepage()

    if authorized_user == " ":
        print("You must be logged in to donate")
    else:
        print("Logged in as:", authorized_user)

    option = input("Choose an option between 1-5: ")
    if option == "1":
        username = input("\nEnter username:")
        password = input("Enter Password:")
        authorized_user = login(database, username, password)
    elif option == "2":
        username = input("\nEnter username:")
        password = input("Enter Password:")
        authorized_user = register(database, username)
        if authorized_user not in database:
            database[username] = password
    elif option == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("\nPlease choose valid option!")