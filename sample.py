
a=8
b=9
print(a+b)

name ="python"
print(f"hi {name}")

# This is a sample Python file

# name = input("enter your name: ")
# print("Hello, " + name + "!")

# a = "hello jatin"
# print (a)
# print (a)
# print (a)
# print (a)


# item_count = 4
# item_count += 1
# print(item_count)

# x = input("enter a value: ")
# print("You entered: " + x)
# y = input("enter another value: ")
# print("You entered: " + y)

# x,y,z = input("enter three values separated by a space: ").split()
# print("You entered: " + x)
# print("You entered: " + y)
# print("You entered: " + z)


# name = [0]
# name = "python"
# a = name[1:4]
# print(a)


#arithmetic operator   +,-,*,/,%

a = 15
b= 4

print ("addition", a + b)
print ("subtraction", a - b)
print ("multiplication", a * b)
print ("division", a / b)
print ("modulus", a % b)
print ("exponentiation", a ** b)
print ("floor division", a // b)


def calculator():
    count = int(input("How many numbers do you want to enter? "))

    numbers = []
    for i in range(count):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    operation = input(
        "Choose operation (+, -, *, /): "
    )

    result = numbers[0]

    for num in numbers[1:]:
        if operation == "+":
            result += num
        elif operation == "-":
            result -= num
        elif operation == "*":
            result *= num
        elif operation == "/":
            if num == 0:
                print("Error: Division by zero is not allowed.")
                return
            result /= num
        else:
            print("Invalid operation!")
            return

    print("Result:", result)


calculator()
