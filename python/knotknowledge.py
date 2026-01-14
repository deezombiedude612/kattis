n = int(input())
all_knots = set(map(int, input().split()))
learned_knots = set(map(int, input().split()))

print(list(all_knots-learned_knots)[0])
