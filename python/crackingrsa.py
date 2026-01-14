def is_prime(num):
	for i in range(2, num // 2):
		if num % i == 0:
			return False

	return True


def two_prime_factors(n):
	for i in range(2, n // 2):
		if n % i == 0 and is_prime(i):
			if is_prime(n // i):
				return [i, n // i]

	return -1


def main():
	# number of use cases, t
	t = 0

	while not 1 <= t <= 50:
		t = int(input())

	for _ in range(t):
		"""
		n = p x q, p and q are prime, 2 <= p, q <= 1000
		e: encryption constant
		d: decryption constant, unique
		NOTE: de may not fit into Java's int32
		"""
		n = e = 0
		while True:
			user_input = input()
			if len(user_input.split()) == 2:
				[n, e] = [int(x) for x in user_input.split()]
				break

		"""
		determine p and q first
		-> if two_prime_factors(n) give -1, no prime factor pair found, abort
		"""
		if two_prime_factors(n) == -1:
			# print("Invalid n")
			continue
		[p, q] = two_prime_factors(n)

		# phi(n) = phi(p) * phi(q) = (p-1)(q-1)
		phi_n = (p - 1) * (q - 1)

		"""
		de mod phi(n) == 1, find d
		Brute force
		"""
		for d_test in range(2, phi_n):
			if (d_test * e) % phi_n == 1:
				print(d_test)
				break


if __name__ == "__main__":
	main()
