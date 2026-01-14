N = int(input())
num_string = input()
num_list = [int(num) for num in num_string.split()][:N]
print(sum(num_list))
