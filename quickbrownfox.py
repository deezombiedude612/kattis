"""
Kattis Problem: https://open.kattis.com/problems/quickbrownfox
"""

n = int(input())

str_lst = []
for _ in range(n):
    this_str = input()
    str_lst.append(
        "".join(list(filter(lambda char: char not in ['.', ',', '?', '!', "'", '"'], this_str))).lower())

for this_str in str_lst:
    remainder = "".join(sorted(
        list(set(list("abcdefghijklmnopqrstuvwxyz")) - set(this_str))))
    print("pangram" if not remainder else f"missing {remainder}")
