import sys

class MountainBase:
    def __init__(self, key):
        self.key = key
        self.connected_bases = []

    def neighbors(self):
        return self.connected_bases

class MountainMap:
    def __init__(self):
        self.bases = {}

    def add_route(self, departure, arrival):
        if departure not in self.bases:
            self.bases[departure] = MountainBase(departure)
        if arrival not in self.bases:
            self.bases[arrival] = MountainBase(arrival)
        self.bases[departure].connected_bases.append(arrival)

    def __getitem__(self, key):
        if key not in self.bases:
            self.bases[key] = MountainBase(key)
        return self.bases[key]

def dfs_search_routes(mountain_map, current_base, target_base, max_days, current_day, visited_bases):
    if current_day > max_days:
        return 0
        
    if current_base == target_base:
        return 1
        
    successful_routes = 0
    visited_bases.add(current_base)
    
    for neighbor in mountain_map[current_base].neighbors():
        if neighbor not in visited_bases:
            successful_routes += dfs_search_routes(
                mountain_map, neighbor, target_base, max_days, current_day + 1, visited_bases
            )
            
    visited_bases.remove(current_base)
    
    return successful_routes

def main():
    raw_input = sys.stdin.read().split()
    if not raw_input:
        return
        
    total_bases = int(raw_input[0])
    total_routes_count = int(raw_input[1])
    start_base = int(raw_input[2])
    target_base = int(raw_input[3])
    max_days = int(raw_input[4])
    
    mountain_map = MountainMap()
    
    current_index = 5
    for _ in range(total_routes_count):
        source = int(raw_input[current_index])
        destination = int(raw_input[current_index + 1])
        mountain_map.add_route(source, destination)
        current_index += 2
        
    visited_bases = set()
    total_valid_paths = dfs_search_routes(
        mountain_map, start_base, target_base, max_days, 0, visited_bases
    )
    
    print(total_valid_paths)

if __name__ == "__main__":
    main()