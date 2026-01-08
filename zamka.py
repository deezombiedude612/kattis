"""
Kattis Problem: https://open.kattis.com/problems/zamka
"""

# user_input = input()
# L, D, X = [int(i) for i in user_input.split()]
# L, D, X = [int(i) for i in input().split()]
L = int(input())
D = int(input())
X = int(input())


def sum_of_digits(num: int) -> int:
    return sum(int(i) for i in str(num))


# N is minimal number whose sum of digits equal X
# M is maximal number whose sum of digits equal X
for i in range(L, D+1):
    if sum(int(j) for j in str(i)) == X:
        print(i)
        break

for i in range(D, L-1, -1):
    if sum(int(j) for j in str(i)) == X:
        print(i)
        break
