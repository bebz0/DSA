import sys
sys.setrecursionlimit(100000)
class BinaryTree:
    def __init__(self, key=None, left=None, right=None):
        self.mKey = key
        self.mLeftChild = None
        self.mRightChild = None
        self.mMin = float('-inf')
        self.mMax = float('inf')

        if left is not None:
            self.setLeft(left)
        if right is not None:
            self.setRight(right)

    def empty(self):
        return self.mKey is None and self.mLeftChild is None and self.mRightChild is None

    def hasLeft(self):
        return self.mLeftChild is not None

    def hasRight(self):
        return self.mRightChild is not None

    def setLeft(self, item):
        if isinstance(item, BinaryTree):
            self.mLeftChild = item
        else:
            self.mLeftChild = BinaryTree(item)

    def setRight(self, item):
        if isinstance(item, BinaryTree):
            self.mRightChild = item
        else:
            self.mRightChild = BinaryTree(item)

    def ValPath(self, seq, idx):
        if idx == len(seq):
            return True
        next_key = seq[idx]

        if next_key < self.mKey:
            if next_key <= self.mMin:
                return False
            self.setLeft(next_key)
            self.mLeftChild.mMin = self.mMin
            self.mLeftChild.mMax = self.mKey
            
            return self.mLeftChild.ValPath(seq, idx + 1)
            
        elif next_key > self.mKey:
            if next_key >= self.mMax:
                return False
            self.setRight(next_key)
            self.mRightChild.mMin = self.mKey
            self.mRightChild.mMax = self.mMax
            return self.mRightChild.ValPath(seq, idx + 1)
        else:
            return False

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    seq = [int(x) for x in input_data]
    root = BinaryTree(seq[0])
    if root.ValPath(seq, 1):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()