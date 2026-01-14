"""
Bubble Sort Question
"""

user_input = input()
seq = [int(i) for i in user_input.split()]

is_ascending = False
while not is_ascending:
    is_ascending = True

    for i in range(len(seq) - 1):
        if seq[i] > seq[i+1]:
            is_ascending = False
            seq[i], seq[i+1] = seq[i+1], seq[i]
            print(' '.join([str(i) for i in seq]))
