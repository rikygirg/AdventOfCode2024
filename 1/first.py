with open("1/input.txt", 'r') as file:
    lines = [line.strip() for line in file]

array1 = []
array2 = []
for line in lines:
    array1.append(int(line.split("   ")[0]))
    array2.append(int(line.split("   ")[1]))

array1.sort()
array2.sort()

result = 0
for i in range(len(array1)):
    result += abs(array1[i] - array2[i])

print(result)