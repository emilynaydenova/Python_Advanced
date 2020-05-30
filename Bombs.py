n = int(input())

a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
bombs = [[int(p)for p in pp.split(',')] for pp in input().split()]

for i in range(len(bombs)):
    row, column = bombs[i]
    value = a[row][column]
    if value > 0:
        points = [
            [row-1, column-1],
            [row-1, column],
            [row-1, column+1],
            [row, column - 1],
            [row, column + 1],
            [row + 1, column - 1],
            [row + 1, column],
            [row + 1, column + 1],
        ]
        a[row][column] = 0
        for m, p in points:
            if 0 <= m < n and 0 <= p < n:
                if a[m][p] > 0:
                    a[m][p] -= value
# print results
cells = 0
sum_of_cells = 0
a_print = []
for i in range(n):
    for j in range(n):
        if a[i][j] > 0:
            sum_of_cells += a[i][j]
            cells += 1

print(f'Alive cells: {cells}')
print(f'Sum: {sum_of_cells}')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
