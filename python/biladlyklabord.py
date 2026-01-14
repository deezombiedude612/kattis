"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S2_AY2526/assignments/nnxpwh/problems/biladlyklabord
"""

s = input()
for letter in sorted(set(s)):
    while letter*2 in s:
        s = s.replace(letter*2, letter)

print(s)
