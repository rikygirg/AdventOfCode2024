from collections import Counter

with open("1/input.txt", 'r') as file:
    lines = [line.strip() for line in file]

array1 = []
array2 = []
for line in lines:
    array1.append(int(line.split("   ")[0]))
    array2.append(int(line.split("   ")[1]))

array1.sort()
counter = Counter(array2)

result = 0
for i in range(len(array1)):
    result += array1[i] * counter[array1[i]]

print(result)