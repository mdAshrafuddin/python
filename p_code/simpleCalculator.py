# Programming make a sample calculator

# This function add two numbers 
def add(num1, num2):
    return num1 + num2

# Function to substract two number
def sub(num1, num2):
    return num1 - num2

# This functions multipication two number
def mul(num1, num2):
    return num1 * num2

# This functions divide two number 
def div(num1, num2):
    return num1 / num2

# This functions exponentiation
def raisePower(num1, num2):
    return num1 ** num2

print("Operation to perform:");
print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
print("5. Raising a power to number");

# This 3 variable assign
choice = int(input("Enter number: "))
num1   = int(input("Enter first number: "))
num2   = int(input("Enter second number: "))

# This addition function
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2)) 

# This subtraction function
elif choice == '2':
    print(num2, '-', num2, '=', sub(num2, num2))

# This multipication function
elif choice == '3':
    print(num1, '*', num2, mul(num1, num2))

# This division function
elif choice == '4':
    print(num1, '/', num2, div(num1, num2))

# This Exponentiation function
elif choice == '5':
    print(num1, '**', num2, raisePower(num1, num2))

else:
    print("Please select a valid input")