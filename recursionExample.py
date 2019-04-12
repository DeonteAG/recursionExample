##this finds the lowest common factor of the numbers entered
def calculate(num1, num2):
    if num1 == num2:
        print(num1,num2)
        return num1
    elif num1 < num2:
        print(num1,num2)
        ##line of recursion
        return calculate(num1, (num2-num1))
    else:
        print(num1,num2)
        ##line of recursion
        return calculate(num2, (num1-num2))
print("Welcome to my recursive program!\nNow enter your two numbers to find the highest common factor!")
def numbers():
    num1 = input("Number 1: ")
    try:
        num1 = int(num1)
    except (ValueError):
        print("Enter an integer!!")
        numbers()
        
    num2 = input("Number 2: ")
    try:
        num2 = int(num2)
    except (ValueError):
        print("Enter an integer!!")
        numbers()
    calculate(num1,num2)
numbers()

