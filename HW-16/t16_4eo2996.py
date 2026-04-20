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
        self.fee = 0

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

    idx = 1
    for i in range(1, n + 1):
        fee = int(input_data[idx])
        k = int(input_data[idx+1])
        
        nodes[i].fee = fee
        for j in range(k):
            child_id = int(input_data[idx + 2 + j])
            nodes[i].addChild(nodes[child_id])
            
        idx += 2 + k

    def get_min_cost(tree_node):
        children = tree_node.getChildren()        
        if not children:
            return tree_node.fee        
        min_cost = float('inf')
        for child in children:
            cost = get_min_cost(child)
            if cost < min_cost:
                min_cost = cost                
        return tree_node.fee + min_cost
    ans = get_min_cost(nodes[1])
    print(ans)

if __name__ == '__main__':
    solve()