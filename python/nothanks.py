"""
Kattis Problem: https://open.kattis.com/problems/nothanks
"""
# solved in IT5003 Lecture 02 (Sem 2510)

input()  # ignore n
a = sorted(list(map(int, input().split())))
ans = a[0]
for i in range(1, len(a)):
    if a[i-1]+1 != a[i]:
        ans += a[i]
print(ans)

"""
NOTE:
- sorted() utilizes merge sort
"""
