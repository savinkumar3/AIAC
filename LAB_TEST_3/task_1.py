# Node class for BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# BST class
class BST:
    def __init__(self):
        self.root = None

    # Insert a key into the BST
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    # Inorder Traversal (Left → Root → Right)
    def inorder(self):
        print("Inorder Traversal:", end=" ")
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=" ")
            self._inorder(node.right)

    # Search for a key in BST
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None:
            return False
        if key == current.key:
            return True
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)


# ------------ USER INPUT SECTION -------------

bst = BST()

# Take input for inserting values
n = int(input("How many values do you want to insert? "))
print("Enter the values:")
for i in range(n):
    val = int(input())
    bst.insert(val)

# Inorder Traversal
bst.inorder()

# Searching values
m = int(input("How many values do you want to search? "))
print("Enter values to search:")
for i in range(m):
    key = int(input())
    found = bst.search(key)
    if found:
        print(f"Search {key}: Found")
    else:
        print(f"Search {key}: Not Found")
