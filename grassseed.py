"""
C: the cost of seed to sow 1 sq. m. of lawn (0 < C <= 100)
L: the number of lawns to sow (0 < L <= 100)

L pairs of positive real numbers: (w, l)
- w: width of lawn (aka w_i; 0 <= w <= 100)
- l: length of lawn (aka l_i; 0 <= l <= 100)

All real numbers are given with at most decimals after the decimal point.
"""

C = float(input())
L = int(input())

# compute total lawn size (in sq. m.)
total_lawn_size = 0
for _ in range(L):
    # e.g., 2 3
    lawn_dimensions = input()
    [w, l] = [float(x) for x in lawn_dimensions.split()]
    total_lawn_size += (w * l)

# print total cost (why :.7f based on sample input and output?)
print("{:.7f}".format(total_lawn_size * C))
