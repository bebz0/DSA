import sys

class Node:
    def __init__(self, item):

        self.item = item
        self.next = None
        self.prev = None
class Deque:
    def __init__(self):
        self.front = None 
        self.back = None 
        self._size = 0

    def empty(self):
        return self.front is None and self.back is None

    def push_front(self, item):
        node = Node(item)
        node.next = self.front
        if not self.empty():
            self.front.prev = node
        else:
            self.back = node
        self.front = node
        self._size += 1

    def push_back(self, item):
        node = Node(item)
        node.prev = self.back
        if not self.empty():
            self.back.next = node
        else:
            self.front = node
        self.back = node
        self._size += 1

    def pop_front(self):
        if self.empty():
            return "error"
            
        node = self.front
        item = node.item
        self.front = node.next
        
        if self.front is None:
            self.back = None 
        else:
            self.front.prev = None
            
        del node
        self._size -= 1
        return item

    def pop_back(self):
        if self.empty():
            return "error"
            
        node = self.back
        item = node.item
        self.back = node.prev
        
        if self.back is None:
            self.front = None
        else:
            self.back.next = None
            
        del node
        self._size -= 1
        return item

    def get_front(self):
        if self.empty():
            return "error"
        return self.front.item

    def get_back(self):
        if self.empty():
            return "error"
        return self.back.item

    def get_size(self):
        return self._size

    def clear(self):
        self.front = None
        self.back = None
        self._size = 0


def main():
    deque = Deque()
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue    
        command = parts[0]
        if command == "push_front":
            n = int(parts[1])
            deque.push_front(n)
            print("ok")
            
        elif command == "push_back":
            n = int(parts[1])
            deque.push_back(n)
            print("ok")
            
        elif command == "pop_front":
            print(deque.pop_front())
            
        elif command == "pop_back":
            print(deque.pop_back())
            
        elif command == "front":
            print(deque.get_front())
            
        elif command == "back":
            print(deque.get_back())
            
        elif command == "size":
            print(deque.get_size())
            
        elif command == "clear":
            deque.clear()
            print("ok")
            
        elif command == "exit":
            print("bye")
            break

if __name__ == '__main__':
    main()