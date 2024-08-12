x = y = n = 0

while not 1 <= x < y <= n <= 100:
	user_input = input()
	if len(user_input.split()) != 3:
		continue
	[x, y, n] = [int(x) for x in user_input.split()]

for i in range(1, n+1):
	if i % x == 0 and i % y == 0:
		print("FizzBuzz")
	elif i % x == 0:
		print("Fizz")
	elif i % y == 0:
		print("Buzz")
	else:
		print(i)
