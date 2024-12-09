with open("8/input.txt", 'r') as file:
    matrix = [line.strip() for line in file]


antinodes = []
antennas = {}
m = len(matrix)
n = len(matrix[0])
for i in range(m):
    for j in range(n):
        if matrix[i][j] != '.':
            if matrix[i][j] in antennas:
                antennas[matrix[i][j]].append([i,j])
            else:
                antennas[matrix[i][j]] = [[i,j]]
    
antinodes = []
for ant in antennas.values():
    for a in ant:
        for b in ant:
            if a != b:
                antinode = [2*a[0] - b[0], 2*a[1] - b[1]]
                if antinode[0] in range(0, m) and antinode[1] in range(0, n) and antinode not in antinodes:
                    antinodes.append(antinode)

print(len(antinodes))