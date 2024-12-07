def read_grid(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid

def count_word_occurrences(grid, word):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
        (0, -1),          (0, 1),    # Left,       Right
        (1, -1),  (1, 0),  (1, 1)    # Down-left, Down, Down-right
    ]

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                matched = True
                for k in range(word_length):
                    nx, ny = x + dx * k, y + dy * k
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] != word[k]:
                            matched = False
                            break
                    else:
                        matched = False
                        break
                if matched:
                    count += 1
    return count

if __name__ == "__main__":
    grid = read_grid('4/input.txt')
    word = 'XMAS'
    total_occurrences = count_word_occurrences(grid, word)
    print(f'The word "{word}" appears {total_occurrences} times in the grid.')