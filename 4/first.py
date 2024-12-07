with open("4/input.txt", 'r') as file:
    matrix = [line.strip() for line in file]

count = 0
m = len(matrix)
n = len(matrix[0])
for i in range(m):
    for j in range(n):
        if matrix[i][j] == "X":
            if j+3 < n:
                if matrix[i][j+1] == "M" and matrix[i][j+2] == "A" and matrix[i][j+3] == "S":
                    count += 1
            if j-3 >= 0:
                if matrix[i][j-1] == "M" and matrix[i][j-2] == "A" and matrix[i][j-3] == "S":
                    count += 1
            if i+3 < m:
                if matrix[i+1][j] == "M" and matrix[i+2][j] == "A" and matrix[i+3][j] == "S":
                    count += 1
            if i-3 >= 0:
                if matrix[i-1][j] == "M" and matrix[i-2][j] == "A" and matrix[i-3][j] == "S":
                    count += 1
            if i+3 < m and j+3 < n:
                if matrix[i+1][j+1] == "M" and matrix[i+2][j+2] == "A" and matrix[i+3][j+3] == "S":
                    count += 1
            if i-3 >= 0 and j-3 >= 0:
                if matrix[i-1][j-1] == "M" and matrix[i-2][j-2] == "A" and matrix[i-3][j-3] == "S":
                    count += 1
            if i+3 < m and j-3 >= 0:
                if matrix[i+1][j-1] == "M" and matrix[i+2][j-2] == "A" and matrix[i+3][j-3] == "S":
                    count += 1
            if i-3 >= 0 and j+3 < n:
                if matrix[i-1][j+1] == "M" and matrix[i-2][j+2] == "A" and matrix[i-3][j+3] == "S":
                    count += 1

        
print(count)

"""

 s  s  s
  a a a
   mmm
 samXmas
   mmm
  a a a
 s  s  s

"""