TREE_SIZE = 4


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class BinarySearchTree:
    def __init__(self, values=None):
        self.root = None
        if values:
            for value in values:
                self.add(value)

    def inorder(self):
        if not self.root:
            return None
        self.inorder_node(self.root)

    def inorder_node(self, node):
        if node.left:
            self.inorder_node(node.left)
        print(node.value, end=" ")
        if node.right:
            self.inorder_node(node.right)

    def add(self, val):
        if not self.root:
            self.root = Node(val)
            return
        return self.add_node(self.root, val)

    def add_node(self, node, val):
        if val < node.value:
            if not node.left:
                node.left = Node(val)
            else:
                self.add_node(node.left, val)
        else:
            if not node.right:
                node.right = Node(val)
            else:
                self.add_node(node.right, val)

    def find(self, val):
        node = self.root
        while node and node.value != val:
            if val < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def min_value_node(self, node):
        if node.left:
            return self.min_value_node(node.left)
        return node.value

    def delete(self, val):
        if not self.root:
            return self.root
        return self.delete_node(self.root, val)

    def delete_node(self, node, val):
        if val < node.value and node.left:
            node.left = self.delete_node(node.left, val)
        elif val > node.value and node.right:
            node.right = self.delete_node(node.right, val)
        else:
            if not node.left and not node.right:
                return None

            elif not node.left:
                return node.right

            elif not node.right:
                return node.left

            else:
                min_value = self.min_value_node(node.right)
                node.value = min_value
                node.right = self.delete_node(node.right, min_value)

        return node

    def show(self):
        print()
        return self.show_node(self.root, 0)

    def show_node(self, node, space=0):
        if not node:
            return
        space += TREE_SIZE
        self.show_node(node.right, space)
        print(' '*(space-TREE_SIZE), end=" ")
        print(node.value)
        self.show_node(node.left, space)


class AVLTree:
    def add(self, values):
        node = None
        for value in values:
            node = self.add_node(node, value)
        return node

    def add_node(self, node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self.add_node(node.left, value)
        else:
            node.right = self.add_node(node.right, value)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        balanceFactor = self.get_balance(node)
        if balanceFactor > 1:
            if value < node.left.value:
                return self.right_rotation(node)
            else:
                node.left = self.left_rotation(node.left)
                return self.right_rotation(node)

        if balanceFactor < -1:
            if value > node.right.value:
                return self.left_rotation(node)
            else:
                node.right = self.right_rotation(node.right)
                return self.left_rotation(node)

        return node

    def delete_node(self, node, value):
        if not node:
            return node
        elif value < node.value:
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.min_value_node(node.right)
            node.value = temp.value
            node.right = self.delete_node(node.right,
                                          temp.value)
        if node is None:
            return node

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        balanceFactor = self.get_balance(node)
        if balanceFactor > 1:
            if self.get_balance(node.left) >= 0:
                return self.right_rotation(node)
            else:
                node.left = self.left_rotation(node.left)
                return self.right_rotation(node)
        if balanceFactor < -1:
            if self.get_balance(node.right) <= 0:
                return self.left_rotation(node)
            else:
                node.right = self.right_rotation(node.right)
                return self.left_rotation(node)
        return node

    def left_rotation(self, node):
        child = node.right
        grandchild = child.left
        child.left = node
        node.right = grandchild
        node.height = 1 + max(self.get_height(node.left),
                           self.get_height(node.right))
        child.height = 1 + max(self.get_height(child.left),
                           self.get_height(child.right))
        return child

    def right_rotation(self, node):
        child = node.left
        grandchild = child.right
        child.right = node
        node.left = grandchild
        node.height = 1 + max(self.get_height(node.left),
                           self.get_height(node.right))
        child.height = 1 + max(self.get_height(child.left),
                           self.get_height(child.right))
        return child

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def find(self, node, val):
        while node and node.value != val:
            if val < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def show_tree(self, node, space=0):
        if not node:
            return
        space += TREE_SIZE
        self.show_tree(node.right, space)
        print(' '*(space-TREE_SIZE), end=" ")
        print(node.value)
        self.show_tree(node.left, space)


if __name__ == '__main__':
    print("Binary Search Tree: ")
    tree = BinarySearchTree([19, 52, 12, 74, 21, 84, 10, 11])
    tree.add(9)
    tree.inorder()
    tree.show()
    tree.delete(74)
    tree.delete(19)
    tree.delete(99)
    print("\nAfter delete(74): ")
    tree.show()

    print("===========")

    print("AVL Tree: ")
    avltree = AVLTree()
    node = None
    values = [19, 52, 12, 74, 21, 84, 10, 11]
    for value in values:
        node = avltree.add_node(node, value)
    avltree.show_tree(node)
    node = avltree.delete_node(node, 74)
    print("\nAfter delete(74): ")
    avltree.show_tree(node)
