"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S2_AY2526/assignments/nnxpwh/problems/hitastig
"""

n = int(input())
a = list(map(int, input().split()[:n]))

print(max(a), min(a))
