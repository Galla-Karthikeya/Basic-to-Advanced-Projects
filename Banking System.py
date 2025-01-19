import random
import string

def password_generator():
    letters = string.ascii_letters
    digits = string.digits
    total = list(letters + digits)
    random.shuffle(total)
    password = random.sample(total, 10)
    return "".join(password)

data = {}
user_amount = {}


def sendoff():
    print("Thankyou for Visiting GTS Bank\nVisit Again.")
    return

def withdraw(username):
    if username not in user_amount.keys():
        war = input("You have not deposited any amount in GTS Bank\nDo you want to create now (Yes/No): ").lower()
        if war == 'yes':
            deposit(username)
        else:
            return sendoff()
    else:
        amount = float(input("Enter the Amount to withdraw: "))
        while user_amount[username] < amount:
            amount = float(input(f"The withdraw amount is more than your Balance, your Balance is {user_amount[username]} Try again: "))
        user_amount[username] -= amount
        print(f"Your Bank Balance is {user_amount[username]}")
    return bank(username)


def deposit(username):
    amount = float(input("Enter the Amount to Deposit: "))
    if username not in user_amount.keys():
        while amount < 500:
            amount = float(input("The money should be min of 500$: "))
        user_amount[username] = amount
        print(f"Your Bank Balance is {user_amount[username]}")
    else:
        print(f"Your Bank Balance is {user_amount[username]}")
        user_amount[username] += amount
        print(f"After Update Balance is {user_amount[username]}")
    return bank(username)
    

def balance(username):
    if username not in user_amount.keys():
        war = input("You have not deposited any amount in GTS Bank\nDo you want to create now (Yes/No): ").lower()
        if war == 'yes':
            deposit(username)
        else:
            return sendoff()
    else:
        print(f'Hi {username}, your Bank Balance is {user_amount[username]}')
    return bank(username)

def login():
    username = input("Enter your Name: ")
    if username in data.keys():
        password = input("Enter your Password: ")
        if data[username] == password:
            print("Login Successful.")
            bank(username)
        else:
            print("Incorrect Credentials, Try Again Later.")
            return

def signin():
    username = input("Enter your Name: ")
    pas = input("Enter the password (auto/manual): ").lower()
    if pas == 'auto':
        password = password_generator()
    else:
        password = input()
    data[username] = password
    print(f'Your username is {username}, \nand password is {password}')
    login()
    return username, password
    

def login_query():
    que = input("Do you have an account (Yes/No): ").lower()
    if que == 'no':
        que = input("Do you want to create an account (Yes/No): ").lower()
        if que == 'no':
            return sendoff()
        else:
            return signin()
    else:
        que = input("Do you want to login to your account (Yes/No): ").lower()
        if que == 'no':
            return sendoff()
        else:
            return login()


def bank(username):
    if username not in user_amount.keys():
        war = input("You have to create an account (min: 500$): (Yes/No): ").lower()
        if war == 'yes':
            deposit(username)
        else:
            return sendoff()
    else:
        query = input("What do you want to see (Balance/ Deposit Money/ Withdraw/ Exit): ").lower()
        while query != 'exit':
            if query[:3] == 'bal':
                return balance(username)
            elif query[:3] == 'dep':
                return deposit(username)
            elif query[:3] == 'wit':
                return withdraw(username)

        print(f"\nHii {username}")
        return sendoff()


if __name__ == '__main__':
    print("Hello, Welcome to GTS Bank.")
    login_query()
