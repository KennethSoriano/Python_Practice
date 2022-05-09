def show_homepage():
    print("\n\t===DonateMe Homepage===")
    print("---------------------------------------")
    print("| 1.   Login     | 2.   Register       |")
    print("---------------------------------------")
    print("| 3.   Donate    | 4.   Show Donations |")
    print("---------------------------------------")
    print("|              5.  Exit                |")
    print("---------------------------------------")

show_homepage()

def donate(username):
    donation_amt = input("\nEnter amount to donate:\t")
    donation_string = username + " donated $" + donation_amt
    print(f"Thank you {username} for your donation of ${donation_amt}!")
    return donation_string

def show_donations(donations):
    print("\n\t--- All Donations---")
    if donations == [ ]:
        print("Currently, there are no donations.")
    else:
        print(donations)
