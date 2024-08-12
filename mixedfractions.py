def main():
	while True:
		user_input = input()
		if user_input == "0 0":
			break
		if len(user_input.split()) != 2:
			continue

		[numerator, denominator] = [int(x) for x in user_input.split()]
		if not 1 <= numerator <= 2 ** 31 - 1 or not 1 <= denominator <= 2 ** 31 - 1:
			continue

		quotient = numerator // denominator
		remainder_numerator = numerator % denominator
		print(f"{quotient} {remainder_numerator} / {denominator}")


if __name__ == "__main__":
	main()
