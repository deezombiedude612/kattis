for _ in range(int(input())):
    P, R, F = map(int, input().split())
    year = 0
    while P <= F:  # IS THIS SLOW OR FAST?
        year += 1
        P *= R
    print(year)
