N = int(input())
simon_instructions = []

for _ in range(N):
    instr = input()
    if instr[:10].strip() == "Simon says":
        simon_instructions.append(instr[10:].strip())

for instr in simon_instructions:
    print(instr)
