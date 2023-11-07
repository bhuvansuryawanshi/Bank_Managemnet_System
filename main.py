class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.widthdrawcash = False
        self.name = ""

    def register(self, name, phone, password):
        cash = self.cash
        conditions = True
        if len(str(phone)) != 10:
            print("Invalid Phone number! Please enter a 10-digit number")
            conditions = False

        if len(password) < 5 or len(password) > 18:
            print("Enter a password greater than 5 and less than 18 characters")
            conditions = False

        if conditions:
            print("Account created successfully")
            self.client_details_list = [name, phone, password, cash]
            with open(f"{name}.txt", "w") as f:
                for details in self.client_details_list:
                    f.write(str(details) + "\n")

    def login(self, name, password):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if password == self.client_details_list[2]:
                self.loggedin = True

            if self.loggedin:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name

            else:
                print("Wrong details")

    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]), str(self.cash)))

            print("Amount added successfully")

        else:
            print("Enter a correct amount")

    def withdraw_cash(self, amount, name, password):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if password == self.client_details_list[2]:
                self.widthdrawcash = True

        if self.widthdrawcash:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]), str(total_cash)))

            with open(f"{self.name}.txt", "r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]), str(left_cash)))

            print("Amount Withdrawn Successfully")
            print("Balance left =", left_cash)
            self.cash = left_cash

    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("Enter a password greater than 5 and less than 18 characters")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[2]), str(password)))
            print("New Password set successfully")

    def phone_change(self, phone):
        if len(str(phone)) != 10:
            print("Invalid Phone number! Please enter a 10-digit number")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[1]), str(phone)))
            print("New Phone number set up successfully")


if __name__ == "__main__":

    Bank_object = Bank()

    print("WELCOME TO THE BANK")
    print("---------------------------")
    print("1. Login")
    print("2. Create a new Account")
    print("Type 'exit' to quit")
    print("---------------------------")

    while True:
        user = input("Choose option 1 or 2: ")

        if user == '1':
            print("Logging in")
            name = input("Enter Name: ")
            password = input("Enter password: ")
            Bank_object.login(name, password)

            while Bank_object.loggedin:
                print("--------------------")
                print("1. Add amount")
                print("2. Check Balance")
                print("3. Withdraw amount")
                print("4. Edit profile")
                print("5. Logout")
                print("--------------------")
                login_user = input()

                if login_user == '1':
                    print("Balance =", Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)
                    print("\n1. Back to menu")
                    print("2. Logout")
                    choose = input()
                    if choose == '1':
                        continue
                    elif choose == '2':
                        break

                elif login_user == '2':
                    print("Balance =", Bank_object.cash)
                    print("\n1. Back to menu")
                    print("2. Logout")
                    choose = input()
                    if choose == '1':
                        continue
                    elif choose == '2':
                        break

                elif login_user == '3':
                    print("Balance =", Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    if 0 <= amount <= Bank_object.cash:
                        name = input("Enter name: ")
                        password = input("Enter password: ")
                        Bank_object.withdraw_cash(amount, name, password)
                        print("\n1. Back to menu")
                        print("2. Logout")
                        choose = input()
                        if choose == '1':
                            continue
                        elif choose == '2':
                            break
                    elif amount < 0:
                        print("Enter a positive value for the amount")
                    elif amount > Bank_object.cash:
                        print("Not enough balance")

                elif login_user == '4':
                    print("1. Password change")
                    print("2. Phone Number change")
                    edit_profile = input()
                    if edit_profile == '1':
                        new_password = input("Enter new Password: ")
                        Bank_object.password_change(new_password)
                        print("\n1. Back to menu")
                        print("2. Logout")
                        choose = input()
                        if choose == '1':
                            continue
                        elif choose == '2':
                            break
                    elif edit_profile == '2':
                        new_ph = int(input("Enter new Phone Number: "))
                        Bank_object.phone_change(new_ph)
                        print("\n1. Back to menu")
                        print("2. Logout")
                        choose = input()
                        if choose == '1':
                            continue
                        elif choose == '2':
                            break

                elif login_user == '5':
                    print("Logout Successful")
                    Bank_object.loggedin = False

        elif user == '2':
            print("Creating a new Account")
            name = input("Enter Name: ")
            phone = int(input("Enter Phone Number: "))
            password = input("Enter password: ")
            Bank_object.register(name, phone, password)

        elif user == 'exit':  # Exit condition
            break
        else:
            print("Invalid input. Please enter 1, 2, or 'exit'.")

    
        