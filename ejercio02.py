class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def inorder(self):
        result = []
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            result.append(node.val)
            _inorder(node.right)
        _inorder(self.root)
        return result

    def height(self):
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

def build_balanced_bst(sorted_values):
    if not sorted_values:
        return None
    mid = len(sorted_values) // 2
    root = TreeNode(sorted_values[mid])
    root.left = build_balanced_bst(sorted_values[:mid])
    root.right = build_balanced_bst(sorted_values[mid + 1:])
    return root

def balance_bst(bst):
    sorted_values = bst.inorder()
    balanced_root = build_balanced_bst(sorted_values)
    balanced_bst = BinarySearchTree()
    balanced_bst.root = balanced_root
    return balanced_bst

def test_balance_bst():
    # 🌳 Balanced tree
    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)
    
    # 📐➡️ Right-skewed tree
    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)
    
    # 📐⬅️ Left-skewed tree
    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)

    # Balance them
    balanced1 = balance_bst(bst1)
    balanced2 = balance_bst(bst2)
    balanced3 = balance_bst(bst3)

    # Validations
    print(bst1.inorder() == balanced1.inorder() and balanced1.height() <= bst1.height())  # True
    print(bst2.inorder() == balanced2.inorder() and balanced2.height() <= bst2.height())  # True
    print(bst3.inorder() == balanced3.inorder() and balanced3.height() <= bst3.height())  # True

test_balance_bst()
