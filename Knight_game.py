n = int(input())
# initialize chess desk
a = []
for i in range(n):
    a.append([ch for ch in input()])
deleted = 0  # K -> 0
# Knight(кон) is moving in the shape of L
while True:
    max_points = 0
    point = [0, 0]
    for i in range(n):
        for j in range(n):
            # max possible 8 positions
            points = [
                [i-1, j-2],
                [i+1, j-2],
                [i-2, j-1],
                [i-2, j+1],
                [i-1, j+2],
                [i+1, j+2],
                [i+2, j+1],
                [i+2, j-1],
            ]
            if a[i][j] == 'K':
                count = 0
                for [m, p] in points:
                    if 0 <= m < n and 0 <= p < n:
                        if a[m][p] == 'K':
                            count += 1
                if count > max_points:
                    point = [i, j]
                    max_points = count

    if max_points == 0:
        break
    else:
        x = point[0]
        y = point[1]
        a[x][y] = '0'
        deleted += 1

print(deleted)
