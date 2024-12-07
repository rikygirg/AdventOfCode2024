with open("2/input.txt", 'r') as file:
    lines = [line.strip() for line in file]

reports = []
for line in lines:
    reports.append([int(i) for i in line.split(" ")])

def check_report(report) -> bool:
    difference = report[0] - report[-1]
    unsafe = 0
    for i in range(1,len(report)):
        if difference < 0:
            if report[i] - report[i-1] < 1 or report[i] - report[i-1] > 3:
                unsafe = True
        else:
            if report[i-1] - report[i] < 1 or report[i-1] - report[i] > 3:
                unsafe = True
    return not unsafe

safe_count = 0
for report_ in reports:
    if check_report(report_):
        safe_count += 1
        continue
    for j in range(len(report_)):
        report = report_[:j] + report_[j+1:]
        if check_report(report):
            safe_count += 1
            break
        

print(safe_count)