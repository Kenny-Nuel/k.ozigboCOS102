import math

print("Quadratic Equation or Cubic Equation (Q or C) ")
response = input("> ")

if response.lower() == 'q':
    print("a")
    a = int(input("> "))

    print("b")
    b = int(input("> "))

    print("c")
    c = int(input("> "))

    numerator = ((b ** 2) - (4 * a * c)) ** 0.5
    denominator = 2 * a

    first_root = ((-1 * b) + numerator) / denominator
    second_root = ((-1 * b) + numerator) / denominator

    print(f"The roots of the equation are x = {first_root} or {second_root}")

elif response.lower() == 'c':
    print("a")
    a = int(input("> "))

    print("b")
    b = int(input("> "))

    print("c")
    c = int(input("> "))

    print("d")
    d = int(input("> "))

    i = 1

    while i < 11:
        calculation = ((a) * (i ** 3)) + ((b) * (i ** 2)) + (c * i) + d
        if calculation == 0:
            print(f" x = {i}")
        else:
            break

        i += 1

else:
    print("Invalid input")