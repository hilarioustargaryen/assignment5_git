turns = int(input("Enter turns: "))

negative = 0
positive = 0
pos_sum = 0
neg_sum = 0

for x in range(0, turns, 1):
    value = int(input("Enter value: "))
    if value < 0:
        negative += 1
        neg_sum += value
    else:
        positive += 1
        pos_sum += value

print("Negatives: ", negative, "Negatives sum: ", neg_sum)
print("Positives: ", positive, "Positives sum: ", pos_sum)