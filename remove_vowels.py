import re


x = input("write your string: ")

split_string = re.split("[aeiouAEIOU]", x)

y = " ".join(split_string)

z = re.split(r"\W+", y)

print(" ".join(z))