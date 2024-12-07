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
    for i in range(len(nums)):
        if not correct:
            break
        for rule in rules:
            if rule[1] == nums[i]:
                if rule[0] in nums[i:]:
                    correct = False
                    break
    if correct:
        sum += nums[int(len(nums)/2)]

print(sum)