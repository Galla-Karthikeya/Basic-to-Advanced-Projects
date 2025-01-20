def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def pro(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
def powr(x,y):
    return x**y

def calculator():
    opr = input("What operation do you want to perform (add, sub, product, division, modulus, power, square): ").lower()
    if opr[:3] == 'squ':
        x = int(input("Enter the number: "))
        val = lambda x: x**2
        return val(x)
    x = eval(input("Enter the first number: "))
    y = eval(input("Enter the second number: "))
    print(x, y)
    if opr[:3] == 'add':
        return add(x,y)
    elif opr[:3] == 'sub':
        return sub(x,y)
    elif opr[:3] == 'pro':
        return pro(x,y)
    elif opr[:3] == 'div':
        return div(x,y)
    elif opr[:3] == 'mod':
        return mod(x,y)
    elif opr[:3] == 'pow':
        return powr(x,y)
    else:
        return 'Enter Correct Operator.'


if __name__ == '__main__':
    print(calculator())