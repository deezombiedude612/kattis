"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S2_AY2526/assignments/nnxpwh/problems/mork
"""


n = int(input())    # number of goals scored
m = int(input())    # number of teams scored (0, 1, 2)

if m == 0:
    print("Jebb")
elif m == n == 2:
    print("Jebb")
else:
    print("Neibb")
