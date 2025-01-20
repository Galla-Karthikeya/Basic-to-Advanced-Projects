import string
import random

def password_generator():
    letters = string.ascii_letters
    digits = string.digits
    total = list(letters+digits)
    random.shuffle(total)
    count = int(input("Enter how many digit password you required: "))
    return "".join(random.sample(total, count))

if __name__ == '__main__':
    print(f'Your Password is {password_generator()}')