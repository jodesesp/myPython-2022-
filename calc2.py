#esto es una calculadora

def menu():

    print("-----")
    print("Mult(x)")
    print("-----")
    print("Div(/)")
    print("-----")

while True:

    user = input(">> ")


    if user == "x":
        num1 = int(input("num1 "))
        num2 = int(input("num2 "))
        calc = num1 * num2
        total = print(f"total = {calc}")

    if user == "/":
        num1 = int(input("num1 "))
        num2 = int(input("num2 "))
        calc = num1 / num2
        total = print(f"total = {calc}")
