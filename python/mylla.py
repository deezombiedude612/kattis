"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S2_AY2526/assignments/nnxpwh/problems/mylla
"""

N = int(input())  # number of rounds needed to win the bet
S = input()       # winners of a series of games

A = H = temp_a = temp_h = 0
for g in S:
    # increment score based on who won the current game `g`
    temp_a += int(g == 'A')
    temp_h += int(g == 'H')

    # round ends when it is clear who will win best of 5 games
    if temp_a >= 3 or temp_h >= 3:
        # increment round score based on who had the most wins in the current round
        A += int(temp_a > temp_h)
        H += int(temp_h > temp_a)

        # reset the counter before starting a new round
        temp_a = temp_h = 0

    if A >= N or H >= N:
        break

# print the loser's name
if A >= N:
    print("Hannes")
elif H >= N:
    print("Arnar")
