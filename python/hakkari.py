"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S2_A2526/assignments/nnxpwh/problems/hakkari
"""

n, m = map(int, input().split()[:2])
grid = []
for i in range(n):
    row = input()
    grid.append(row[:m])

mines = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            mines.append((i+1, j+1))

print(len(mines))
for m in mines:
    print(*m)
