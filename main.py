import os
import time

#
projectVersion = 1.3
adminLogin = False


def adminLogin_Check():
    adminLogin_verify = input(f"Please enter the admin login code: ")
    if adminLogin_verify == "password":
        print("password accepted!")
        main(adminLogin=True)
    else:
        print(f"This is incorrect!")
        adminLogin_Check()


def generatePassword():
    print(f"Generate password func")
    time.sleep(2)

    passwordType_select = input(f"")


# Main true loop
def main(adminLogin):
    if adminLogin != True:
        adminLogin_Check()
    else:
        while True:
            time.sleep(2.5)
            # Main menu loop
            mainMenu_Input = input(f"Choose an option: "
                                   f"\n\t1. Generate a password"
                                   f"\n\t2. View passwords"
                                   f"\n\t3. View accounts"
                                   f"\n\t4. Add account"
                                   f"\n\t5. Delete account"
                                   f"\n\t6. Show help "
                                   f"\n\t7. Options"
                                   f"\n\t8. Exit"
                                   f"\n\nEnter input: ")
            # Check if input is valid
            try:
                useroption = int(mainMenu_Input)
            except ValueError:
                print(f"Not a digit")
                main()

            # Check if input is valid
            if useroption not in (1, 2, 3, 4, 5, 6, 7, 8):
                print(f"Please select a valid option!")
                main()
            match useroption:
                # Generate password
                case 1:
                    generatePassword()
                # View passwords
                case 2:
                    print("> View password")
                    continue
                # View accounts
                case 3:
                    print("> View accounts")
                    continue
                # Add account
                case 4:
                    print("> Add account")
                    continue
                # Delete account
                case 5:
                    print("> Delete account")
                    continue
                # Help menu
                case 6:
                    print("> Open help menu")
                    continue
                # Application options
                case 7:
                    print("> Options")
                    continue
                # Exit program
                case 8:
                    quit()


main(adminLogin)
