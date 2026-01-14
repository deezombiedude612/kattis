int_list = []

for _ in range(10):
    int_input = int(input())
    int_list.append(int_input % 42)

print(len(set(int_list)))
