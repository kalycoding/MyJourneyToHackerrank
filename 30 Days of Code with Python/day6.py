string = 'ptvzstvotxqyvzrwyqryzrpkswzryupwutmigc'
e = ''
o = ''
for i in range(len(string)):
    if i % 2 == 0:
        e = e + string[i]
for j in range(len(string)):
    if j % 2 != 0:
        o = o + string[j]

print(e + " " + o)
