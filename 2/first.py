with open("2/input.txt", 'r') as file:
    lines = [line.strip() for line in file]

reports = []
for line in lines:
    reports.append([int(i) for i in line.split(" ")])

safe_count = 0
for report in reports:
    difference = report[0] - report[-1]
    #print(report, difference)
    if abs(difference) < len(report) or abs(difference) > 3*len(report):
        continue
    unsafe = False
    for i in range(1,len(report)):
        if difference < 0:
            if report[i] - report[i-1] < 1 or report[i] - report[i-1] > 3:
                unsafe = True
        else:
            if report[i-1] - report[i] < 1 or report[i-1] - report[i] > 3:
                unsafe = True
    if not unsafe:
        safe_count += 1

print(safe_count)