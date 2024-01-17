class AVLNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1  

def height(node):
    return node.height if node else 0

def is_avl_balanced(node):
    if not node:
        return True

    balance = height(node.left) - height(node.right)

    if abs(balance) > 1:
        return False

    return is_avl_balanced(node.left) and is_avl_balanced(node.right)




root = AVLNode(10)
root.left = AVLNode(5)
root.right = AVLNode(20)
root.left.left = AVLNode(2)
root.left.right = AVLNode(7)
root.right.left = AVLNode(15)
root.right.right = AVLNode(25)

print("Is the AVL tree balanced?", is_avl_balanced(root))

root.left.left.left = AVLNode(1)

print("Is the AVL tree balanced after introducing imbalance?", is_avl_balanced(root))

