import itertools

with open("7/input.txt", 'r') as file:
    lines = [line.strip() for line in file]

calibrations = []
for line in lines:
    line = line.split(":")
    nums = [int(line[0])]
    for num in line[1].split(" "):
        if num != "":
            nums.append(int(num))
    calibrations.append(nums)

sum = 0
for cal in calibrations:
    N = len(cal)-2
    combinations = itertools.product(['+','*','||'], repeat=N)
    for oper in combinations:
        result = cal[1]
        for i in range(len(oper)):
            if oper[i] == '+':
                result += cal[2+i]
            elif oper[i] == '*':
                result *= cal[2+i]
            else:
                result = int(str(result) + str(cal[2+i]))
            i += 1
        if result == cal[0]:
            sum += result
            break
print(sum)
        