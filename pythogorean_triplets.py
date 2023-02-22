a = int(input("first value: "))
b = int(input("second value: "))
c = int(input("third value: "))

if a**2 + b**2 == c**2:
    print("it is a pythagorean triplets")
    print(f"{a}^(2) + {b}^(2) = {c}^(2)")
else:
    print("it is not a pythagorean triplets.")
    print(f"{a}^(2) + {b}^(2) = {c}^(2)")