"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S2_A2526/assignments/nnxpwh/problems/mylla
Incomplete

"""

N = int(input())
S = input()

A, H = 0, 0  # rounds won by Arnar and Hannes respectively

# number of games won in that round (each round has 5 games)
temp_a = temp_h = 0
for i in range(len(S)):
    temp_a += int(S[i] == 'A')
    temp_h += int(S[i] == 'H')

    if i % 5 == 4:
        A += int(temp_a > temp_h)
        H += int(temp_h > temp_a)
        temp_a = temp_h = 0

        if A == 2:
            print("Hannes")
            break
        elif H == 2:
            print("Arnar")
            break
