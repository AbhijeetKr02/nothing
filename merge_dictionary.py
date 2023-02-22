sectionB = {
    "Name": input("Enter Name: "),
    "Roll no.": input("Enter Roll no.: ")
}
sectionA = {
    "Name1": input("Enter Name: "),
    "Roll no1.": input("Enter Roll no.: ")
}

if input("Want to change section (y for yes n for no): ").lower() == "y":
    for key, value in sectionA.items():
        sectionB.update({key:value})

print(sectionB)