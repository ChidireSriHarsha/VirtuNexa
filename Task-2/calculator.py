def add(x, y): return x + y
def divide(x, y): return x / y if y != 0 else "Error"

while True:
    op = input("Enter +, -, *, / or q to quit: ")
    if op == 'q': break
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    result = {
        '+': add(x, y),
        '/': divide(x, y)
    }.get(op, "Invalid operation")
    print("Result:", result)
