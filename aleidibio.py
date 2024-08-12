def main():
	a = b = c = 0

	while a < 1 or a > 100:
		# a = int(input("Enter number of mins to drive from Hannes to Amar >> "))
		a = int(input())

	while b < 1 or b > 100:
		# b = int(input("Enter number of mins to drive from Amar to cinema >> "))
		b = int(input())

	while c < 720 or c > 1439:
		# c = int(input("Enter minute of the day on which film is scheduled to start >> "))
		c = int(input())

	print(c - a - b)


if __name__ == "__main__":
	main()
