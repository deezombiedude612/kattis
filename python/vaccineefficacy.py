"""
Kattis Problem: https://open.kattis.com/problems/vaccineefficacy
https://nus.kattis.com/problems/vaccineefficacy
"""

# N: number of participants
# each participant is indicated with a 4-char string (either 'Y' or 'N')
# - first letter indicates if participant has been vaccinated
# - last 3 letters indicate infection by strains A, B and C respectively ('Y' means infected)

N = int(input())
participants = [input().strip() for _ in range(N)]

# print(participants)

infected_count = [[0, 0, 0], [0, 0, 0],]  # vaccinated, unvaccinated

for p in participants:
    group = int(p[0] == 'N')
    infected_count[group] = [infected_count[group][i] + int(p[i+1] == 'Y')
                             for i in range(len(p[1:]))]

print(infected_count)

for i in range(3):
    efficacy = [(infected_count[0][i] + infected_count[1][i]) / N * 100
                for i in range(len(infected_count[0]))]
    print(efficacy)
