"""
n: number of bags, 1 <= n <= 10^5
k: Benni's bag number, -10^9 <= k <= 10^9

a: list of n bag numbers (k must always be inside; for 1 <= i <= n, -10^9 <= a_i <= 10^9)
"""
n_and_k = input()
n_and_k = [int(x) for x in n_and_k.split()]
# print(n_and_k)

a = input()
a = [int(x) for x in a.split()]

if a[0] == n_and_k[1]:
    print("fyrst")
elif a[1] == n_and_k[1]:
    print("naestfyrst")
else:
    for i in range(2, len(a)):
        if a[i] == n_and_k[1]:
            print((i + 1), "fyrst")
