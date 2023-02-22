number = input("enter number: ")

x = 0
for i in number:
    x += int(i)**len(number)

if number == str(x):
    print("number is an armstrong number")
else:
    print("not an armstrong number.")