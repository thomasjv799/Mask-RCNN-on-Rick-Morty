def add(x, y)
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    print("Cannot divide by zero!")
  return x / y

print("Simple Math Application")
print("-----------------------")

while True:
  num1 = input("Enter first number: ")
  num1 = int(num1)

  operator = input("Enter operator (+, -, *, /): ")

  num2 = input("Enter second number: ")
  num2 = int(num2)

  if operator == "+":
    result = add(num1, num2)
  else if operator == "-":
    result = subtract(num1, num2)
  else if operator == "*":
    result = multiply(num1, num2)
  else if operator == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operator!")

  print(f"The result is: {result}")

  again = input("Do you want to perform another calculation? (y/n): ")
  if again.lower() != "y":
    break

print("Thank you for using the Simple Math Application!")
