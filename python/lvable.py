"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S1_AY2627/assignments/hkm5gk/problems/lvable
"""

int(input())    # this is redundant input
word = input().strip()
print(0 if "lv" in word else 1 if 'l' in word or 'v' in word else 2)

# I THOUGHT TOO HARD >:(

# input_len = int(input())
# input_str = input()

# num_ops = 0

# while "lv" not in input_str:
#     if 'l' in input_str and 'v' in input_str:
#         l_index = input_str.find('l')
#         v_index = input_str.find('v')

#         if l_index < v_index:
#             # 'l' before 'v': if 1 character in between, remove that character
#             #                 otherwise, reverse substring from 'l' to before 'v'
#             if abs(v_index - l_index) == 2:
#                 input_str = input_str[:l_index+1] + input_str[v_index:]
#             else:
#                 input_str = input_str[:l_index] + \
#                     input_str[l_index:v_index-1:-1] + input_str[v_index:]
#         else:
#             # 'v' before 'l': reverse substring "v..l"
#             input_str = input_str[:v_index] + \
#                 input_str[l_index:v_index-1:-1] + input_str[l_index+1:]
#     elif 'l' in input_str:
#         if input_str[-1] == 'l':
#             # 'l' at the end: append 'v'
#             input_str += 'v'
#         else:
#             # 'l' not at the end: replace next character with 'v'
#             l_index = input_str.find('l')
#             input_str = input_str[:l_index+1] + 'v' + input_str[l_index+2:]
#     elif 'v' in input_str:
#         if input_str[0] == 'v':
#             # 'v' in front: prepend 'l'
#             input_str = 'l' + input_str
#         else:
#             # 'v' not in front: replace previous character with 'l'
#             v_index = input_str.find('v')
#             input_str = input_str[:v_index-1] + 'l' + input_str[v_index:]
#     else:
#         # 'lv', 'l', 'v' nowhere to be found: append 'lv' to the end
#         input_str += "lv"

#     num_ops += 1


# print(num_ops)
