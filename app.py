import os
import random
import string

passwords = {}

#load passwords from file
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            site, pwd = line.strip().split(":")
            passwords[site] = pwd

except FileNotFoundError:
    print("No passwords found. Starting with an empty password manager.")

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%&^"
    password = "".join(random.choice(chars) for _ in range(length))
    return password


     

while True:
    print("\n ----Password Manager----")

    print("Press 1 to find your passwords")
    print("Press 2 to save new password")
    print("Press 3 to update your password")
    print("Press 4 to generate password")
    print("Press 5 to view all your passwords")
    print("press 6 to exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter the site name: ")
        if site in passwords:
            print(f"Your {site} password is: {passwords[site]}")
        else:
            print(f"{site} does not exist")    


    elif choice == "2":
        site = input("Enter the site name: ")
        pwd = input("Enter the password: ")
        passwords[site] = pwd
        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")
        print(f"Your {site} password has been saved successfully!")    

    elif choice == "3":
        site = input("Enter the site name: ")
        new_pwd = input("Enter the new password: ")
        if site in passwords:
            passwords[site] = new_pwd
            with open("passwords.txt", "w") as file:
                for s, p in passwords.items():
                    file.write(f"{s}:{p}\n")
            print(f"Your {site} password has been updated successfully!")
        else:
            print(f"{site} does not exist")


    elif choice == "4":
        length = int(input("Enter the desired password length: "))
        new_pass = generate_password(length)
        print(f"Generated password: {new_pass}")
        print("Now copy paste the password to save in your password manager")

    elif choice == "5":
        if passwords:
            print("Your saved passwords:")
            for site, pwd in passwords.items():
                print(f"{site}: {pwd}")
        else:
            print("No passwords saved yet.")        
                    

    elif choice == "6":
        print("Exiting.....")
        break
    else:
        print("Invalid choice. Please try again.")