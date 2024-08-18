input_string = input()

vowel_count = 0
for i in input_string.lower():
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

print(vowel_count)
