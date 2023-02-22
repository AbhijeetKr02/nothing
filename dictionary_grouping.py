#dictionary grouping
from itertools import groupby
Student = [{"student": "Manhvi", "marks": 96},
        {"student": "krish", "marks": 57},
        {"student": "Abhijeet", "marks": 2},
        {"student": "Advaita", "marks": 85},
        {"student": "Ansh", "marks": 75}
]
def key_func(k):
    return k["student"]
Student = groupby(Student, key= key_func)
print(Student)

for key, group in Student:  
    print(key) 
    for value in group:
        print(value)