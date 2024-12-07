with open("5/input.txt", 'r') as file:
    data = [line.strip() for line in file]

rules = []
prints = []
blank_flag = False
for line in data:
    if line == "":
        blank_flag = True
    elif blank_flag:
        prints.append([int(a) for a in line.split(",")])
    else:
        rules.append([int(a) for a in line.split("|")])

sum = 0
for nums in prints:
    correct = True
    i = 0
    while i < len(nums):
        redo = False
        for rule in rules:
            if rule[1] == nums[i]:
                for j in range(i+1, len(nums)):
                    if rule[0] == nums[j]:
                        nums[i] = rule[0]
                        nums[j] = rule[1]
                        correct = False
                        redo = True
                        break
        if not redo:
            i += 1
    if not correct:
        sum += nums[int(len(nums)/2)]

print(sum)