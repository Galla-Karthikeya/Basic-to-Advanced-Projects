import random

def hint(count, val):
    str_val = str(val)
    if count == 0:
        guess = int(input("Give any number: "))
        if guess == val:
            print("You guess the correct answer.")
        elif guess < val:
            print("You need to move forward to find a number.")
        else:
            print("You need to move backward to find a number.")
    elif count == 1:
        print(f"The number is in {str_val[0]} series")
    elif count == 2:
        print(f'The number is in between {val-2} and {val+2}')
    return count+1

def guess():
    count = 0
    val = random.randint(1, 100)
    print(val)
    chances = int(input("No of Chances you required: "))
    num = 1
    while(num <= chances):
        guess = eval(input(f"Chance {num}: \nGuess a Number: (Press hint) "))
        print(guess)
        if guess == 'hint':
            if count > 3:
                return
            count = hint(count, val)
        else:
            if guess == val:
                print(f'You Guess the right number {guess}')
                if count == 0:
                    print("Your Score is 100")
                elif count == 1:
                    print('Your Score is 75')
                else:
                    print('Your Score is 50')
                return
            elif val < guess:
                print('Your Guess greater than actual, try again.')
            elif val > guess:
                print("Your Guess is less than actual, try again.")
            num += 1
    return "Done With the Chances, You Lost the Game."

if __name__ == '__main__':
    print(guess())