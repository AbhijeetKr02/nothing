
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_n(numbers):
    gcd_value = numbers[0]
    for i in range(1, len(numbers)):
        gcd_value = gcd(gcd_value, numbers[i])
    return gcd_value

no_of_input = int(input("Enter no. of input: "))

list_number = []
n = 1
while no_of_input > 0:
    list_number.append(int(input(f"Enter Number{n}: ")))
    no_of_input -= 1
    n += 1
list_number = sorted(list_number)
print(f"The greatest integer is: {gcd_n(list_number)}")
