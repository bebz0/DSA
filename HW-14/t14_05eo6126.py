import sys

class Node:
    def __init__(self, item):
        self.item = item 
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None 
        self._size = 0 

    def empty(self):
        return self.front is None and self.back is None

    def push(self, item):
        new_node = Node(item)
        if self.empty():
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node
        self._size += 1

    def pop(self):
        if self.empty():
            return "error"
            
        current_front = self.front
        item = current_front.item
        self.front = self.front.next
        del current_front 
        
        if self.front is None:
            self.back = None 
            
        self._size -= 1
        return item

    def get_front(self):
        if self.empty():
            return "error"
        return self.front.item

    def get_size(self):
        return self._size

    def clear(self):
        self.front = None
        self.back = None
        self._size = 0


def main():
    queue = Queue()
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        command = parts[0]
        if command == "push":
            n = int(parts[1])
            queue.push(n)
            print("ok")
            
        elif command == "pop":
            print(queue.pop())
            
        elif command == "front":
            print(queue.get_front())
            
        elif command == "size":
            print(queue.get_size())
            
        elif command == "clear":
            queue.clear()
            print("ok")
            
        elif command == "exit":
            print("bye")
            break

if __name__ == '__main__':
    main()