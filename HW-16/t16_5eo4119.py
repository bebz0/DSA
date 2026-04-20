import sys
class Node:
    def __init__(self, key=None):
        self.mKey = key

    def empty(self):
        return self.mKey is None

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey

class Tree(Node):
    def __init__(self, key=None):
        super().__init__(key)
        self.mChildren = []

    def empty(self):
        return super().empty() and len(self.mChildren) == 0

    def addChild(self, child):
        self.mChildren.append(child)

    def removeChild(self, key):
        for child in self.mChildren:
            if child.key() == key:
                self.mChildren.remove(child)
                return True
        return False

    def getChild(self, key):
        for child in self.mChildren:
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        return self.mChildren


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    paths = input_data[1:n+1]
    root = Tree("ROOT")
    for path in paths:
        parts = path.split('\\')
        current = root
        for part in parts:
            next_node = current.getChild(part)
            if next_node is None:
                next_node = Tree(part)
                current.addChild(next_node)
            current = next_node

    def DFS_print(tree_node, depth):
        children = tree_node.getChildren()
        children.sort(key=lambda child: child.key())
        for child in children:
            print(" " * depth + child.key())
            DFS_print(child, depth + 1)

    DFS_print(root, 0)

if __name__ == '__main__':
    solve()