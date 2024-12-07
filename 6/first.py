with open("6/input.txt", 'r') as file:
    matrix = [line.strip() for line in file]

m = len(matrix)
n = len(matrix[0])
visited_tiles = []
for i in range(m):
    if not len(visited_tiles):
        for j in range(n):
            if matrix[i][j] == '^':
                visited_tiles.append([i,j])
                break


i = visited_tiles[-1][0]
j = visited_tiles[-1][1]
go = 1
direction = '^'
while go:
    if direction == '^':
        if i == 0:
            go = False
        elif matrix[i-1][j] == '.' or matrix[i-1][j] == '^':
            i = i-1
            visited_tiles.append([i, j])
        else:
            direction = '>'
    elif direction == 'v':
        if i == m-1:
            go = False
        elif matrix[i+1][j] == '.' or matrix[i+1][j] == '^':
            i = i+1
            visited_tiles.append([i, j])
        else:
            direction = '<'
    elif direction == '>':
        if j == n-1:
            go = False
        elif matrix[i][j+1] == '.' or matrix[i][j+1] == '^':
            j = j+1
            visited_tiles.append([i, j])
        else:
            direction = 'v'
    elif direction == '<':
        if j == 0:
            go = False
        elif matrix[i][j-1] == '.' or matrix[i][j-1] == '^':
            j = j-1
            visited_tiles.append([i, j])
        else:
            direction = '^'

visited_once = []
for tile in visited_tiles:
    if tile not in visited_once:
        visited_once.append(tile)

print(len(visited_once))