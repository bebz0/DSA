import sys

def solve(N, tracks):
    best_sum = -1
    best_path = []
    founded = False
    
    def search(idx, curr_sum, remain_sum, curr_path):
        nonlocal best_sum, best_path, founded
        if founded:
            return
        if curr_sum > best_sum:
            best_sum = curr_sum
            best_path = curr_path[:]
            if curr_sum == N:
                founded = True
                return
                
        if idx == len(tracks):
            return
        if curr_sum + remain_sum <= best_sum:
            return
            
        track_len = tracks[idx]
        if curr_sum + track_len <= N:
            curr_path.append(track_len)
            search(idx + 1, curr_sum + track_len, remain_sum - track_len, curr_path)
            curr_path.pop()
        search(idx + 1, curr_sum, remain_sum - track_len, curr_path)

    search(0, 0, sum(tracks), [])
    
    return best_path, best_sum

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    it = iter(input_data)
    
    while True:
        try:
            N = int(next(it))
            num_tracks = int(next(it))
            tracks = [int(next(it)) for _ in range(num_tracks)]
            path, total = solve(N, tracks)
            print(f"sum:{total}")
            
        except StopIteration:
            break

if __name__ == '__main__':
    main()