# BST 개별 노드

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# search 함수
# 루트가 null이거나 키가 있을 때
def search(root, key):
    if root is None or root.val == key:
        return root

# 키가 루트의 키 값보다 클 때
    if root.val < key:
        return search(root.right, key)
# 키가 루트의 키 값보다 작을 때
    return search(root.left, key)

# insert 함수
# 키를 가진 새 노드

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root

# 중위순회 함수
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

    #    50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)