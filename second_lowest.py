list_student = []

for i in range(int(input("Enter no. of students: "))):
    data = {
        "Name": input("Enter Name: "),
        "Grade": float(input("Enter grades: "))
    }
    list_student.append(data)

key = "Grade"

updated_list = []
for item in list_student:
    if item[key] not in [x[key] for x in updated_list]:
        updated_list.append(item)

new_list = sorted(updated_list, key = lambda x:x["Grade"])

print(f"""
Second lowest grade scored by:
{new_list[1]['Name']}: {new_list[1]['Grade']}
""")
        
        




