import sys

class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]

def solve():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    
    while idx < len(data):
        n = data[idx]
        idx += 1
        if n == 0:
            break
        while data[idx] != 0:
            target = data[idx : idx + n]
            idx += n
            
            stat = Stack()
            com = 1
            
            for exp in target:
                while com <= n and (stat.empty() or stat.peek() != exp):
                    stat.push(com)
                    com += 1
                    
                if not stat.empty() and stat.peek() == exp:
                    stat.pop()
            if stat.empty():
                print("Yes")
            else:
                print("No")
                
        print()
        idx += 1

if __name__ == "__main__":
    solve()