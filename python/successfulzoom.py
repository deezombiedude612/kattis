"""
Kattis Problem: https://open.kattis.com/problems/successfulzoom

n: 2 <= n <= 10^5
x: list of integers 0 <= x_i <= 2^30
    i: positive integers up to n
"""


n = int(input())
x = list(map(int, input().split()))

smallest_k = None

for k in range(1, n):
    x_2 = x[k-1::k]
    # print(x_2)
    if len(x_2) < 2:
        break
    # if sorted(x_2) == x_2:
    if all(x_2[i] < x_2[i+1] for i in range(len(x_2)-1)):   # non-decreasing
        smallest_k = k
        break

print(smallest_k if smallest_k is not None else "ABORT!")
