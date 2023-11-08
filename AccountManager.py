#Create a program that will read the files and create dictionaries. Add infromation about users from file to the dictionaries.
def import_and_create_bank(filename):
    '''function for reading a file and creating bank accounts in dictionaries'''

    bank = {}

    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        lst = line.strip().split(':')
        if len(lst) <= 1:
            continue

        key = lst[0].strip()
        value = lst[1].strip()

        try:
            value = float(value)
            bank[key] = bank.get(key, 0) + value
        except:
            continue
    f.close()

    return bank
def valid(password):
    '''function that checks username's password if it's valid'''

    if len(password) < 8:
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def signup(user_accounts, log_in, username, password):
    '''function that allows users to sign up.'''

    if username in user_accounts:
        if log_in.get(username):
            return False
        #if not valid(password):
        #    return False
        #previous_passwords = user_accounts.get(username, [])
        #if password in previous_passwords:
        #    return False
        #previous_passwords.append(password)
        #user_accounts[username] = previous_passwords
    else:
        if log_in.get(username):
            return False
        if not valid(password):
            return False
        if username == password:
            return False
        user_accounts[username] = password
        log_in[username] = False
        return True

def import_and_create_accounts(filename):
    '''this function is used to create an user accounts dictionary and another login dictionary'''

    user_accounts = {}
    log_in = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                lst = line.strip().split('-')
                if len(lst) <= 1:
                    continue

                username = lst[0].strip()
                password = lst[1].strip()

                if not valid(password):
                    continue

                if username not in user_accounts:
                    user_accounts[username] = password
                    log_in[username] = False

    except FileNotFoundError:
        print(f"File '{filename}' is not found")

    return user_accounts, log_in

def login(user_accounts, log_in, username, password):
    '''function for log in to your account'''

    if username in user_accounts and user_accounts[username] == password:
        log_in[username] = True
        return True
    else:
        return False

def update(bank, log_in, username, amount):
    '''function that updates the value of your bank account'''

    if username in log_in and log_in[username] and username in bank:
        if bank[username] + amount >= 0:
            bank[username] += amount
            return True
    elif username not in bank:
        bank[username] = 0
        if bank[username] + amount >= 0:
            bank[username] += amount
        return True
    return False

def transfer(bank, log_in, userA, userB, amount):
    '''function that allows you to transfer money from one user (that need to be logged in) to the second'''

    if userA in bank and log_in.get(userA):
        if userB in log_in:
            if bank[userA] >= amount:
                bank[userA] -= amount
                bank[userB] = bank.get(userB, 0) + amount
                return True
    return False

def change_password(user_accounts, log_in, username, old_password, new_password):
    '''function that allows you to change your password'''

    if username in user_accounts and log_in.get(username) and user_accounts[username] == old_password and old_password != new_password and valid(new_password):
        user_accounts[username] = new_password
        return True
    return False

def delete_account(user_accounts, log_in, bank, username, password):
    '''function that allows you to delete your account'''

    if username in user_accounts and log_in.get(username) and password == user_accounts[username]:
        del user_accounts[username]
        del log_in[username]
        if username in bank:
            del bank[username]
        return True
    return False

def main():
    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password)
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break
        else:
            print("The option is not valid. Please re-enter the option.\n")


if __name__ == '__main__':
    main()
