with open("4/input.txt", 'r') as file:
    matrix = [line.strip() for line in file]

count = 0
m = len(matrix)
n = len(matrix[0])
for i in range(1,m-1):
    for j in range(1,n-1):
        if matrix[i][j] == "A":
            if matrix[i-1][j-1] == "M" and matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" and matrix[i+1][j+1] == "S":
                count += 1
            if matrix[i-1][j-1] == "M" and matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S" and matrix[i+1][j+1] == "S":
                count += 1
            if matrix[i-1][j-1] == "S" and matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" and matrix[i+1][j+1] == "M":
                count += 1
            if matrix[i-1][j-1] == "S" and matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S" and matrix[i+1][j+1] == "M":
                count += 1

        
print(count)

"""

M S
 A
M S

"""