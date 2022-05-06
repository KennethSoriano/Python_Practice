from donations_pkg.homepage import show_homepage

database = { "admin": "password123"}
donations = [ ]
authorized_user = " "

while True:
    show_homepage()

    if authorized_user == " ":
        print("You must be logged in to donate")
    else:
        print("Logged in as:", authorized_user)

    option = input("Choose an option")
    if option == "1":
        print("TODO: Write Login Functionality")
    if option == "2":
        print("TODO: Write Register Functionality")
    elif option == "3":
        print("TODO: Write Donate Functionality")
    elif option == "4":
        print("TODO: Write Show Donations Functionality")
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Please choose valid option!")