"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S2_AY2526/assignments/nnxpwh/problems/grafaholur

`n` workers take `h` hours to dig out `x` cubic meters
`m` workers take ??? hours to dig out `y` cubic meters
"""

n = int(input())
h = int(input())
x = int(input())
m = int(input())
y = int(input())

ans = h * n / m / x * y
print(ans)
