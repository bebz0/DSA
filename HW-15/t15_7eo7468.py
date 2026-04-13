import sys

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def ReorderList(self) -> None:
        if self.head is None or self.head.next is None:
            return

        left = self.head
        right = self.tail

        while True:
            next_left = left.next
            prev_right = right.prev

            if left == right:
                left.next = None
                self.tail = left
                break
            
            if left.next == right:
                right.next = None
                self.tail = right
                break

            left.next = right
            right.next = next_left
            left = next_left
            right = prev_right

    def Print(self) -> None:
        curr = self.head
        while curr is not None:
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
        lst.addToTail(int(input_data[i]))
    lst.ReorderList()
    lst.Print()

if __name__ == '__main__':
    main()