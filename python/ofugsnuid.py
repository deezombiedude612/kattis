num_ints = int(input())
int_list = []
for i in range(num_ints):
    user_input = int(input())
    int_list.append(user_input)

for i in range(len(int_list) - 1, -1, -1):
    print(int_list[i])
