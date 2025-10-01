"""
Kattis Problem: https://open.kattis.com/problems/estimatingtheareaofacircle
"""

from math import pi

rmc_list = []
while True:
    user_input = input().split()
    r = float(user_input[0])
    m, c = tuple(map(int, user_input[1:]))

    if r == m == c == 0:
        break

    rmc_list.append((r, m, c))

for r, m, c in rmc_list:
    area = pi * r**2
    dot_shtuff = c/m * (r*2)**2
    dot_shtuff = int(dot_shtuff) if int(
        dot_shtuff) == dot_shtuff else dot_shtuff

    print(area, dot_shtuff)
