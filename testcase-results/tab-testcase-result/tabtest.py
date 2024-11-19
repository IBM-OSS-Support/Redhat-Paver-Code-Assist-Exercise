#simple calculator using python

def add(x,y) : return x+y
def subtract(x,y) : return x-y

def multiply(x,y) : return x*y
def divide(x,y) : return x/y

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1m, num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")[{"name": "add", "arguments": {"x": 5.0, "y": 3.0}}, {"name": "subtract", "arguments": {"x": 10.0, "y": 4.0}}, {"name": "multiply", "arguments": {"x": 2.0, "y": 6.0}}, {"name": "divide", "arguments": {"x": 8.0, "y": 2.0}}]