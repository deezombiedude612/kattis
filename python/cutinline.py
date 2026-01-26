"""
Kattis Problem Demo in IT5003 Lab Week 03 (Arrays)
"""

my_line = list()
for _ in range(int(input())):
    my_line.append(input())


# cut e b : place e in front of b
for _ in range(int(input())):
    instr = str.split(input())
    if len(instr) == 3 and instr[0] == 'cut':
        my_line.insert(my_line.index(instr[2]), instr[1])
    elif len(instr) == 2 and instr[0] == 'leave':
        my_line.remove(instr[1])

for item in my_line:
    print(item)
