with open("3/input.txt", 'r') as file:
    lines = [line.strip() for line in file]

text = ""
for line in lines:
    text += line

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sum = 0
last_action = True
for i in range(len(text)-7):
    if text[i:i+4] == "mul(":
        j = i+4
        num1 = ""
        num2 = ""
        first_number = True
        while j < len(text):
            if first_number:
                if text[j] in numbers:
                    num1 += text[j]
                elif text[j] == ",":
                    first_number = False
                else:
                    j = len(text)
            else:
                if text[j] in numbers:
                    num2 += text[j]
                elif text[j] == ")":
                    sum += int(num1)*int(num2) * last_action
                    j = len(text)
                else:
                    j = len(text)
            j += 1
    elif text[i:i+4] == "do()":
        last_action = True
    elif text[i:i+7] == "don't()":
        last_action = False


print(sum)
