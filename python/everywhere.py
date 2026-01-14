"""
Kattis Problem: https://open.kattis.com/problems/everywhere
"""

n = int(input())

distinct_cities = []
for _ in range(n):
    num_visits = int(input())

    cities = set()
    for i in range(num_visits):
        city = input()
        cities.add(city)
    distinct_cities.append(cities)

for s in distinct_cities:
    print(len(s))
