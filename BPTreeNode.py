# bptree.py

class Node:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.values = []
        self.children = []

class BPTree:
    def __init__(self, degree):
        self.degree = degree
        self.root = Node(is_leaf=True)

    def insert(self, key, value):
        root = self.root
        if len(root.keys) == 2 * self.degree - 1:
            new_root = Node()
            new_root.children.append(self.root)
            self.split(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, value)

    def _insert_non_full(self, node, key, value):
        if node.is_leaf:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
            node.values.insert(i + 1, value)
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            child = node.children[i]
            if len(child.keys) == 2 * self.degree - 1:
                self.split(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, value)

    def split(self, parent, i):
        degree = self.degree
        node = parent.children[i]
        new_node = Node(is_leaf=node.is_leaf)
        parent.keys.insert(i, node.keys[degree - 1])
        parent.children.insert(i + 1, new_node)

        new_node.keys = node.keys[degree:]
        node.keys = node.keys[:degree - 1]
        new_node.values = node.values[degree:]
        node.values = node.values[:degree - 1]

        if not node.is_leaf:
            new_node.children = node.children[degree:]
            node.children = node.children[:degree]

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node.values[i]
        elif node.is_leaf:
            return None
        else:
            return self._search(node.children[i], key)
