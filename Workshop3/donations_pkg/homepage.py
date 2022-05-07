def show_homepage():
    print("\t===DonateMe Homepage===")
    print("---------------------------------------")
    print("| 1.   Login     | 2.   Register       |")
    print("---------------------------------------")
    print("| 1.   Donate    | 2.   Show Donations |")
    print("---------------------------------------")
    print("|              5.  Exit                |")
    print("---------------------------------------")

show_homepage()

def donate(username):
    donation_amt = input("Enter amount to donate:")
    donation_string = "{username} donated {donation_amt}"
    print("Thank you for your donation!")
    return donation_string
