import sys

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def RotateRight(self, k: int) -> None:
        if self.head is None or self.head.next is None or k == 0:
            return
            
        length = 1
        curr = self.head
        while curr.next:
            curr = curr.next
            length += 1
            
        k = k % length
        if k == 0:
            return
            
        curr.next = self.head
        steps = length - k
        new_tail = self.head
        for _ in range(steps - 1):
            new_tail = new_tail.next
            
        self.head = new_tail.next
        self.tail = new_tail
        self.tail.next = None

    def Print(self) -> None:
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    lst = List()
    for i in range(1, n + 1):
        lst.AddToTail(int(input_data[i]))
        
    for i in range(n + 1, len(input_data)):
        k = int(input_data[i])
        lst.RotateRight(k)
        lst.Print()

if __name__ == '__main__':
    main()