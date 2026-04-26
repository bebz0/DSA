import sys

class PriorityQueue:
    def __init__(self):
        self.items = [[0, ""]] 
        self.size = 0 
        self.pos = {}

    def empty(self):
        return len(self.items) == 1

    def insert(self, priority, item_id):
        self.size += 1
        self.items.append([priority, item_id])
        self.pos[item_id] = self.size
        self.siftUp(self.size)

    def siftUp(self, i):
        while i > 1:
            parent = i // 2
            if self.items[i][0] > self.items[parent][0]:
                self.swap(parent, i)
                i = parent
            else:
                break

    def extractMaximum(self):
        root = self.items[1]
        del self.pos[root[1]]
        
        self.items[1] = self.items[-1]
        if self.size > 1:
            self.pos[self.items[1][1]] = 1
            
        self.items.pop()
        self.size -= 1
        
        if self.size > 0:
            self.siftDown(1)
            
        return root

    def siftDown(self, i):
        while (2 * i) <= self.size:
            left = 2 * i
            right = 2 * i + 1
            largest = self.maxChild(left, right)
            
            if self.items[i][0] < self.items[largest][0]:
                self.swap(largest, i)
                i = largest
            else:
                break

    def swap(self, i, j):
        self.pos[self.items[i][1]] = j
        self.pos[self.items[j][1]] = i
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def maxChild(self, left, right):
        if right > self.size:
            return left
        else:
            if self.items[left][0] > self.items[right][0]:
                return left
            else:
                return right

    def changePriority(self, item_id, new_prio):
        i = self.pos[item_id]
        old_prio = self.items[i][0]
        self.items[i][0] = new_prio
        
        if new_prio > old_prio:
            self.siftUp(i)
        elif new_prio < old_prio:
            self.siftDown(i)

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    q = PriorityQueue()
    for line in input_data:
        if not line.strip():
            continue
        parts = line.split()
        cmd = parts[0]
        if cmd == "ADD":
            q.insert(int(parts[2]), parts[1])
        elif cmd == "POP":
            res = q.extractMaximum()
            print(f"{res[1]} {res[0]}")
        elif cmd == "CHANGE":
            q.changePriority(parts[1], int(parts[2]))

if __name__ == '__main__':
    main()