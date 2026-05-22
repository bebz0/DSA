
def wave(maze, start, wall_cell):
    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]

    n = len(maze)
    m = len(maze[0])

    waveMatrix = []
    for i in range(n):
        waveMatrix.append([-1] * m)

    sources = []
    for i in range(n):
        sources.append([None] * m)

    q = []
    q.append(start)
    waveMatrix[start[0]][start[1]] = 0

    while len(q) > 0:
        current = q.pop(0)
        i = current[0]
        j = current[1]

        for k in range(4):
            i1 = i + di[k]
            j1 = j + dj[k]

            if 0 <= i1 < n and 0 <= j1 < m:
                if waveMatrix[i1][j1] == -1 and maze[i1][j1] != wall_cell:
                    q.append((i1, j1))
                    waveMatrix[i1][j1] = waveMatrix[i][j] + 1
                    sources[i1][j1] = (i, j)

    return waveMatrix, sources


n = int(input())
maze = []
for i in range(n):
    maze.append(list(input().strip()))

start = (0, 0)
end = (0, 0)

for i in range(n):
    for j in range(n):
        if maze[i][j] == '@':
            start = (i, j)
        elif maze[i][j] == 'X':
            end = (i, j)

waveMatrix, sources = wave(maze, start, 'O')

if waveMatrix[end[0]][end[1]] == -1:
    print("N")
else:
    print("Y")
    curr = end
    while curr != start:
        maze[curr[0]][curr[1]] = '+'
        curr = sources[curr[0]][curr[1]]

    for i in range(n):
        print("".join(maze[i]))

