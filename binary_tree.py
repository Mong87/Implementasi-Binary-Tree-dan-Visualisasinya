from node import Node
from graphviz import Digraph

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

    #traversal
    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    #visual text
    def display_text(self, node, level=0):
        if node is not None:
            self.display_text(node.right, level + 1)
            print(" " * 5 * level + "->", node.data)
            self.display_text(node.left, level + 1)

    #visual graph/diagram
    def display_graph(self):
        dot = Digraph()

        def add_edges(node):
            if node:
                dot.node(str(node.data))
                if node.left:
                    dot.edge(str(node.data), str(node.left.data))
                    add_edges(node.left)
                if node.right:
                    dot.edge(str(node.data), str(node.right.data))
                    add_edges(node.right)

        add_edges(self.root)
        dot.render('binary_tree', view = True, format='png')
        print("Visualisasi diagram berhasil disimpan sebagai 'binary_tree.png'")