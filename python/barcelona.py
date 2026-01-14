"""
n: number of bags, 1 <= n <= 10^5
k: Benni's bag number, -10^9 <= k <= 10^9

a: list of n bag numbers (k must always be inside; for 1 <= i <= n, -10^9 <= a_i <= 10^9)
"""
n_and_k = input()
[n, k] = [int(x) for x in n_and_k.split()]
# print(n_and_k)

a = input()
a = [int(x) for x in a.split()]

if a[0] == k:
    print("fyrst")
elif a[1] == k:
    print("naestfyrst")
else:
    for i in range(2, len(a)):
        if a[i] == k:
            print((i + 1), "fyrst")
