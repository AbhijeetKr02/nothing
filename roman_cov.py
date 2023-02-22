#Convert a roman numeral to an integer
num = int(input("enter number: "))

numeral = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_num = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

roman = ''

i = 0
while  num > 0:
    for _ in range(num // numeral[i]):
        roman += roman_num[i]
        num -= numeral[i]
    i += 1

print(roman)