# Algorthms GUI Project / bst.py
# Created on: 07-Nov-2018
# Author: Gourav Siddhad
# Binary Search Tree

class BST_Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BST():
    def __init__(self):
        self.root = BST_Node(None)
        self.total = 0

    def read_File(self, inputFile):
        with open(inputFile, 'r') as Input:
            for line in Input:
                ints = [int(x) for x in line.split()]
                for v in ints:
                    self.insert(v)

    def insert(self, new_value):
        self.total = self.total + 1
        self.insert_node(BST_Node(new_value))

    def get_total(self):
        return self.total

    def insert_node(self, new_node, current_node=None):
        if current_node is None:
            current_node = self.root

        if current_node.data:
            if new_node.data < current_node.data:
                if current_node.left is None:
                    new_node.parent = current_node
                    current_node.left = new_node
                else:
                    self.insert_node(new_node, current_node.left)
            else:
                if current_node.right is None:
                    new_node.parent = current_node
                    current_node.right = new_node
                else:
                    self.insert_node(new_node, current_node.right)
        else:
            current_node.data = new_node.data
            current_node.left = new_node.left
            current_node.right = new_node.right
            current_node.parent = new_node.parent

    def print_tree(self, current_node=None):
        output = ''
        if current_node is None:
            current_node = self.root
        stack = []
        stack.append(current_node.left)
        stack.append(current_node.right)
        output = str(current_node.data) + ' '
        while stack:
            n = stack.pop(0)
            if n is not None:
                #                 print(n.data, end=' ')
                output = output + str(n.data) + ' '
                stack.append(n.left)
                stack.append(n.right)
            # else:
                #print('Null', end=' ')
        return output

    def lookup(self, data, current_node=None):
        if current_node is None:
            current_node = self.root
        if data < current_node.data:
            if current_node.left is None:
                return None
            return self.lookup(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                return None
            return self.lookup(data, current_node.right)
        else:
            return current_node

    def children_count(self, current_node=None):
        if current_node is None:
            current_node = self.root
        cnt = 0
        if current_node.left:
            cnt += 1
        if current_node.right:
            cnt += 1
        return cnt

    def delete(self, data):
        # get node containing data
        node = self.lookup(data)
        if node is not None:
            children_count = self.children_count(node)
        else:
            return 'Node Not Found'
        parent = node.parent

        if children_count == 0:
            # if node has no children, just remove it
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else:
                self.root = BST_Node()
        elif children_count == 1:
            # if node has 1 child
            # replace node with its child
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            # if root node
            else:
                self.root.left = n.left
                self.root.right = n.right
                self.root.data = n.data
        else:
            # if node has 2 children
            # find its successor
            parent = node
            successor = node.left
            while successor.right:
                parent = successor
                successor = successor.right
            # replace node data by its successor data
            node.data = successor.data
            # fix successor's parent's child
            if parent.right == successor:
                parent.right = successor.left
            else:
                parent.left = successor.left
        return 'Node Deleted'
