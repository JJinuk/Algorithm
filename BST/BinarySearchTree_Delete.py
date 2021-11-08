class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# 중위순회 함수
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def insert(node, key):
    #  트리가 비어있다면, 새로운 노드를 리턴함
    if node is None:
        return node(key)
    # 트리를 재귀적으로 내려감
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    # 노드 포인터 반환
    return node


def minValueNode(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


# BST와 키가 주어지면
# 키를 삭제하고 새 루트 반환

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif key > root.key:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)

        return root


#              50
#           /     \
#          30      70
#         /  \    /  \
#       20   40  60   80

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)

print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)

print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)

print("Inorder traversal of the modified tree")
inorder(root)
