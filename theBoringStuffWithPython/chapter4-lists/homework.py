grid = [['.', '.', '.', '.', '.', '.'],
        ['O', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
a = -1
ab = 0
for g in range(8):
    a += 1
    for g2 in range(6):
        if g2 < 7:
            print(grid[a][ab], end='')
        elif g2 == 7:
            print(grid[a][ab])
        else:
            print(grid[a][ab])

