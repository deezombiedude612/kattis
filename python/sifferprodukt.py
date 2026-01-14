n = abs(int(input()))

# while not 1 <= n < 10:
while n // 10:
    product = 1
    for digit in str(n):
        if int(digit):
            product *= int(digit)

    n = product

print(n)
