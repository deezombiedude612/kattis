"""
Kattis Problem: https://open.kattis.com/problems/multiplication
"""


def hori_border(size):
	size = max(1, size)
	print("+--", end="")
	for i in range(size):
		print("----", end="")
	print("-+")


def hori_grid_border(size):
	size = max(1, size)
	print("| ", end="")
	for i in range(size):
		print("+---", end="")
	print("+ |")


def print_top_number(num):
	size = len(str(num))
	print("top num size:", size)
	print("|   ", end="")
	for i in range(size):
		print(f"{num // 10 ** (size - i - 1)}   ", end="")
		num %= 10 ** (size - i - 1)
	print("|")


def main():
	while True:
		user_input = input()
		numbers = [int(x) for x in user_input.split()]

		# exit if "0 0"
		if numbers == [0, 0]:
			break
		# finish loop execution if not two integers entered
		if len(numbers) != 2:
			print("Enter two integers only!")
			continue

		num0_size = len(str(numbers[0]))
		num1_size = len(str(numbers[1]))

		hori_border(num0_size)

		print_top_number(numbers[0])

		hori_grid_border(num0_size)
		for i in range(num1_size):
			row_result = numbers[0] * int(str(numbers[1])[0])
			# print(numbers[0] * int(str(numbers[1])[0]))

			# row 1 of 3
			print("| ", end="")
			print("|")

			numbers[1] = numbers[1] % 10 ** (num1_size - 1)
			hori_grid_border(num0_size)

		hori_border(num0_size)


if __name__ == "__main__":
	main()
