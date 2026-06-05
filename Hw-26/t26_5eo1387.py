import sys
import math

def solve():
    all_tokens = sys.stdin.read().split()
    if not all_tokens:
        return
    
    token_index = 0
    num_tokens = len(all_tokens)

    while token_index < num_tokens:
        num_points = int(all_tokens[token_index])
        token_index += 1
        
        if num_points == 0:
            break

        points = []
        for _ in range(num_points):
            x = int(all_tokens[token_index])
            y = int(all_tokens[token_index + 1])
            points.append((x, y))
            token_index += 2

        visited = [False] * num_points
        msd = [1e18] * num_points
        
        msd[0] = 0.0
        total_cable_length = 0.0

        for _ in range(num_points):
            curr_point_idx = -1
            best_distance = 1e18
            
            for i in range(num_points):
                if not visited[i] and msd[i] < best_distance:
                    best_distance = msd[i]
                    curr_point_idx = i

            visited[curr_point_idx] = True
            total_cable_length += math.sqrt(best_distance)

            cx, cy = points[curr_point_idx]
            for j in range(num_points):
                if not visited[j]:
                    px, py = points[j]
                    dx = cx - px
                    dy = cy - py
                    sq_dist = dx * dx + dy * dy
                    
                    if sq_dist < msd[j]:
                        msd[j] = sq_dist

        print(f"{total_cable_length:.2f}")

if __name__ == '__main__':
    solve()