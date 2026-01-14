"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S2_AY2526/assignments/nnxpwh/problems/stafsetning

n: number of problems
m: minutes taken for fixing each typo
k: total minutes that can be spent on typos per day
s: list of problems, where s[i] is the number of typos in problem i
"""
from math import ceil

n, m, k = map(int, input().split())
s = map(int, input().split())

# if none of the typos can be done within the time allowed per day
max_typos_per_day = k // m
if max_typos_per_day == 0:
    print(":(")
else:
    # compute minimum days needed
    days_needed = ceil(sum(s) / max_typos_per_day)
    # alternatively, this is a trick to obtain the ceiling value, preferred in competitive programming apparently
    # days_needed = (sum(s) + max_typos_per_day - 1) // max_typos_per_day
    print(days_needed)
