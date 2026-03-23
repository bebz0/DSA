import sys

class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        return self.items.pop()
        
    def back(self):
        if self.empty():
            return "error"
        return self.items[-1]
        
    def size(self):
        return len(self.items)
        
    def clear(self):
        self.items.clear()
        return "ok"

def solve():
    stack = Stack()
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        comm = parts[0]
        
        if comm == "push":
            print(stack.push(int(parts[1])))
        elif comm == "pop":
            print(stack.pop())
        elif comm == "back":
            print(stack.back())
        elif comm == "size":
            print(stack.size())
        elif comm == "clear":
            print(stack.clear())
        elif comm == "exit":
            print("bye")
            break

if __name__ == '__main__':
    solve()