def solve_maze_wallpaper():
    n = int(input())
    maze = [input().strip() for _ in range(n)]
    
    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]
    
    visited = []
    for i in range(n):
        visited.append([False] * n)
        
    q = []
    
    q.append((0, 0))
    visited[0][0] = True
    
    if not visited[n-1][n-1]:
        q.append((n-1, n-1))
        visited[n-1][n-1] = True
        
    while q:
        current = q.pop(0)
        i = current[0]
        j = current[1]
        
        for k in range(len(di)):
            i1 = i + di[k]
            j1 = j + dj[k]
            
            if 0 <= i1 < n and 0 <= j1 < n:
                if maze[i1][j1] == '.' and not visited[i1][j1]:
                    visited[i1][j1] = True
                    q.append((i1, j1))
                    
    faces = 0
    
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                for k in range(len(di)):
                    i1 = i + di[k]
                    j1 = j + dj[k]
            
                    if i1 < 0 or i1 >= n or j1 < 0 or j1 >= n:
                        is_entrance = False
                        
                        if i == 0 and j == 0 and (di[k] == -1 or dj[k] == -1):
                            is_entrance = True
                        elif i == n-1 and j == n-1 and (di[k] == 1 or dj[k] == 1):
                            is_entrance = True
                            
                        if not is_entrance:
                            faces += 1
                            
                    elif maze[i1][j1] == '#':
                        faces += 1
                        
    total_area = faces * 9
    print(total_area)

if __name__ == '__main__':
    solve_maze_wallpaper()