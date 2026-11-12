text = input()

count = 0

for char in text.lower():
    if char in "aeiou" or char in "AEIOU":
        count += 1

print(count)
