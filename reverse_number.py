
number = input("enter number: ")

y = []

for i in number:
    y.append(i)
z = []

for x in range(1, len(y) + 1):
    z.append(y[-x])


w = "".join(z)
print(f"reversed number is: {w}")

