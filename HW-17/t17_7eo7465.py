import sys

class BinaryTree:
    def __init__(self, key=None, left=None, right=None):
        self.mKey = key
        self.mLeftChild = None
        self.mRightChild = None
        
        if left is not None:
            self.setLeft(left)
        if right is not None:
            self.setRight(right)

    def empty(self):
        return self.mKey is None and self.mLeftChild is None and self.mRightChild is None

    def setNode(self, key):
        if isinstance(key, BinaryTree):
            self.mKey = key.mKey
            self.mLeftChild = key.mLeftChild
            self.mRightChild = key.mRightChild
        else:
            self.mKey = key

    def hasLeft(self):
        return self.mLeftChild is not None

    def hasRight(self):
        return self.mRightChild is not None

    def setLeft(self, item):
        if isinstance(item, BinaryTree):
            self.mLeftChild = item
        elif self.hasLeft():
            self.mLeftChild.setNode(item)
        else:
            self.mLeftChild = BinaryTree(item)

    def setRight(self, item):
        if isinstance(item, BinaryTree):
            self.mRightChild = item
        elif self.hasRight():
            self.mRightChild.setNode(item)
        else:
            self.mRightChild = BinaryTree(item)

    def rInsert(self, key):
        if self.empty():
            self.setNode(key)
        else:
            if key < self.mKey:
                if self.hasLeft():
                    self.mLeftChild.rInsert(key)
                else:
                    self.setLeft(key)
            else:
                if self.hasRight():
                    self.mRightChild.rInsert(key)
                else:
                    self.setRight(key)

    def IsSameTree(self, other):
        if other is None or other.empty():
            return 0 if not self.empty() else 1
        if self.mKey != other.mKey:
            return 0
        if self.hasLeft() and other.hasLeft():
            if self.mLeftChild.IsSameTree(other.mLeftChild) == 0:
                return 0
        elif self.hasLeft() or other.hasLeft():
            return 0

        if self.hasRight() and other.hasRight():
            if self.mRightChild.IsSameTree(other.mRightChild) == 0:
                return 0
        elif self.hasRight() or other.hasRight():
            return 0

        return 1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    tree1 = BinaryTree()
    for i in range(1, n + 1):
        tree1.rInsert(int(input_data[i]))
    m_idx = n + 1
    m = int(input_data[m_idx])
    tree2 = BinaryTree()
    for i in range(m_idx + 1, m_idx + 1 + m):
        tree2.rInsert(int(input_data[i]))
    if n != m:
        print(0)
    else:
        print(tree1.IsSameTree(tree2))

if __name__ == '__main__':
    main()