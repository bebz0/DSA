import sys
sys.setrecursionlimit(2000000)
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
        self.color = None 

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
    nodes = [None] + [Tree(key=i) for i in range(1, n + 1)]
    root = None

    idx = 1
    for i in range(1, n + 1):
        p = int(input_data[idx])
        c = int(input_data[idx+1])
        idx += 2

        nodes[i].color = c
        if p == 0:
            root = nodes[i]
        else:
            nodes[p].addChild(nodes[i])

    ans = [0] * (n + 1)
    def DFS(tree_node):
        curr_colors = {tree_node.color}
        for child in tree_node.getChildren():
            child_colors = DFS(child)
            curr_colors.update(child_colors)

        ans[tree_node.key()] = len(curr_colors)
        
        return curr_colors

    if root is not None:
        DFS(root)
    print(*(ans[1:]))

if __name__ == '__main__':
    solve()