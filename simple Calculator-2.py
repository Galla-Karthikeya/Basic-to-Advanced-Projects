def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def product(x,y):
    return x*y
def division(x,y):
    return x/y
def modulus(x,y):
    return x%y
def power(x,y):
    return x**y


def calculator():
    operations = {
        'add': addition,
        'sub': subtraction,
        'pro': product,
        'div': division,
        'mod': modulus,
        'pow': power,
    }
    operation = input("Enter an operator to perform (add, sub, product, division, modulus, power): ")
    if operation[:3] == 'pow':
        x = int(input("Enter a number: "))
        val = lambda x: x**2
        return val(x)
    else:
        x = int(input("Enter the First Number: "))
        y = int(input("Enter the Second Number: "))
        result = operations.get(operation[:3], lambda x, y: 'Invalid Operator')(x,y)
        return result
    
print(calculator())

