"""
    User creating a password with all the criteria 
     https://chatgpt.com/share/672fbaff-2dd0-8003-96bc-7c60890a324e
     used chat to help correct an error of not re-entering the passwrod when failed
"""

import re

def main():

    while True:
        try:
                # Guidelines for the password 
            print("""Password Guidelines:\n
                Between 8 to 20 characters long.\n
                Contains at least one uppercase letter.\n
                Contains at least one lowercase letter.\n
                Includes at least one number.\n
                Includes at least one symbol from the set: !@#$%&*\n""")
                # User input the password they want
            password = input("Please create a new password using the guidelines. ")
                # Seeing if the password is the correct length
            if not (8 <= len(password) <= 20):
                print("The password must be between 8 and 20 characters.")
                continue
                # Seeing if the password contains an uppercase
            if not re.search(r"[A-Z]" , password):
                print ("Password must contain at least one uppercase letter.")
                continue
                # Seeing if the password contains a lowercase
            if not re.search(r"[a-z]" , password):
                print ("Password must contain at least one lowercase letter.")
                continue
                # Seeing if the password contains a number
            if not re.search(r"\d" , password):
                print("Password must contain at least one number.")
                continue
                # Seeing if the password contains any symbol
            if not re.search(r"[!@#$%&*]" , password):
                print("Password must contain at least one symbol.")
                continue    
                # Re-entering the password
            confirm_password = input("Re-enter the password to confirm.")

            if password:
                # comfirming the password is the same as the first password entered
                if password == confirm_password:
                    print("Password Accepted.")
                    return password
                else:
                    print("Passwords do not match. Please try again.")

        except Exception as e:
            print(f"An error has occured: {e}")

main()