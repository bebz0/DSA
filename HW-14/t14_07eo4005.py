import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        return self.front is None

    def push(self, item):
        node = Node(item)
        if self.empty():
            self.front = node
        else:
            self.back.next = node
        self.back = node

    def pop(self):
        if self.empty():
            return None
        item = self.front.item
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return item
if __name__ =="__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        half = n // 2
    
        p1 = Queue()
        for x in data[1:half + 1]:
            p1.push(int(x))
        
        p2 = Queue()
        for x in data[half + 1:]:
            p2.push(int(x))
        
        moves = 0
    
        while not p1.empty() and not p2.empty() and moves < 200000:
            c1 = p1.pop()
            c2 = p2.pop()
        
            if (c1 == 0 and c2 == n - 1) or (c1 > c2 and not (c1 == n - 1 and c2 == 0)):
                p1.push(c1)
                p1.push(c2)
            else:
                p2.push(c1)
                p2.push(c2)
            
            moves += 1
        
        if p1.empty():
            print(f"second {moves}")
        elif p2.empty():
            print(f"first {moves}")
        else:
            print("draw")