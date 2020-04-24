# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
#student_marks = {}
for _ in range(n):
    name, *line = input().split()
    even = name[0:len(name):2]
    odd = name[1:len(name):2]
    print(even + " " + odd)