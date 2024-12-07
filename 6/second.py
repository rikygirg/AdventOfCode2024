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


i = visited_tiles[0][0]
j = visited_tiles[-1][1]
start_pos = [i, j]
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

def printm(matrix, tile):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if [x, y] == tile:
                print('O', end='')
            else:
                print(matrix[x][y], end='')
        print()
    print()


loop_making_tiles = []
for tile in visited_once:
    if tile == start_pos:
        continue
    turns = []
    i = start_pos[0]
    j = start_pos[1]
    go = 1
    direction = '^'
    #print("Cheking tile: ", tile)
    #printm(matrix, tile)
    while go == 1:
        if direction == '^':
            if i == 0:
                go = 0
            elif (matrix[i-1][j] == '.' or matrix[i-1][j] == '^') and [i-1,j] != tile:
                i = i-1
            else:
                if [i,j,direction] in turns:
                    go = -1
                    #print("Gettin out on tile: ", [i,j])
                turns.append([i,j,direction])
                direction = '>'
        elif direction == 'v':
            if i == m-1:
                go = 0
            elif (matrix[i+1][j] == '.' or matrix[i+1][j] == '^') and [i+1,j] != tile:
                i = i+1
            else:
                if [i,j,direction] in turns:
                    go = -1
                    #print("Gettin out on tile: ", [i,j])
                turns.append([i,j,direction])
                direction = '<'
        elif direction == '>':
            if j == n-1:
                go = 0
            elif (matrix[i][j+1] == '.' or matrix[i][j+1] == '^') and [i,j+1] != tile:
                j = j+1
            else:
                if [i,j,direction] in turns:
                    go = -1
                    #print("Gettin out on tile: ", [i,j])
                turns.append([i,j,direction])
                direction = 'v'
        elif direction == '<':
            if j == 0:
                go = 0
            elif (matrix[i][j-1] == '.' or matrix[i][j-1] == '^') and [i,j-1] != tile:
                j = j-1
            else:
                if [i,j,direction] in turns:
                    go = -1
                    #print("Gettin out on tile: ", [i,j])
                turns.append([i,j,direction])
                direction = '^'
    if go == -1:
        loop_making_tiles.append(tile)

print("Total loop made: ", len(loop_making_tiles))