python_students = ['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]

d = {}

for score in python_students:
    d[score[0]] = score[1]

for i,k in d.items():
    print(i,k)
