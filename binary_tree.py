class Node(object):
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree(object):
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(self.root, val)

    def _add(self, node, val):
        if val < node.v:
            if node.l:
                self._add(node.l, val)
            else:
                node.l = Node(val)
        else:
            if node.r:
                self._add(node.r, val)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root:
            return self._find(self.root, val)
        else:
            return None

    def _find(self, node, val):
        return_node = None

        if node.v == val:
            return_node = node
        elif val < node.v and node.l:
            return_node = self._find(node.l, val)
        elif val >= node.v and node.r:
            return_node = self._find(node.r, val)

        return return_node

    def deleteTree(self):
        self.root = None

    def printTree(self):
        self._printTree(self.root)

    def _printTree(self, node):
        if node:
            self._printTree(node.l)
            print node.v
            self._printTree(node.r)


tree = Tree()
tree.add(5)
tree.add(3)
tree.add(2)
tree.add(1)
tree.add(6)
print tree.getRoot()
print tree.find(2)
print tree.find(6)
tree.printTree()


