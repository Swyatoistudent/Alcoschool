import math
from queue import Queue


class TreeNode:
    def __init__(self, value, left=None, right=None, max_height=1):
        self.left = left
        self.right = right
        self.value = value
        self.max_height = max_height


class AVLTree:
    temp = None
    t = 0
    rotation = None

    def __init__(self):
        self.root = None

    def insert(self, val):
        AVLTree.temp = None
        AVLTree.t = 0
        AVLTree.rotation = None
        if self.root is None:
            self.root = TreeNode(val)

        def add(curr, vall):

            if curr is None:
                return None
            if curr.value < vall:
                if curr.right is None:
                    curr.right = TreeNode(vall)
                else:
                    add(curr.right, vall)
            if curr.value > vall:
                if curr.left is None:
                    curr.left = TreeNode(vall)
                else:
                    add(curr.left, vall)
            if curr.left is not None and curr.right is not None:
                curr.max_height = 0
                curr.max_height = max(curr.left.max_height, curr.right.max_height) + 1
            elif curr.left is None and curr.right is not None:
                curr.max_height = 0
                curr.max_height = curr.right.max_height + 1
            elif curr.right is None and curr.left is not None:
                curr.max_height = 0
                curr.max_height = curr.left.max_height + 1

            def LL(node):
                t1 = node.left.right
                x = node
                node = node.left
                node.right = x
                x.left = t1

                return node

            def RR(node):
                t1 = node.right.left
                x = node
                node = node.right
                node.left = x
                x.right = t1
                return node

            if curr.right is None:
                height_r = 0
            else:
                height_r = curr.right.max_height
            if curr.left is None:
                height_l = 0
            else:
                height_l = curr.left.max_height

            def balancing(func):

                if curr.left == AVLTree.temp:
                    curr.left = func
                if curr.right == AVLTree.temp:
                    curr.right = func

            balance = height_r - height_l
            if balance < -1:
                if AVLTree.t != 1:
                    AVLTree.temp = curr
                AVLTree.t = 1
                if AVLTree.temp.left.value > vall:
                    if curr.left == AVLTree.temp or curr.right == AVLTree.temp:
                        balancing(LL(AVLTree.temp))

                if AVLTree.temp.left.value < vall:
                    if curr.left == AVLTree.temp or curr.right == AVLTree.temp:
                        AVLTree.temp.left = RR(AVLTree.temp.left)
                        curr.left = LL(AVLTree.temp)

            if balance > 1:
                if AVLTree.t != 1:
                    AVLTree.temp = curr
                AVLTree.t = 1

                if AVLTree.temp.right.value < vall:
                    if curr.left == AVLTree.temp or curr.right == AVLTree.temp:
                        balancing(RR(AVLTree.temp))

                if AVLTree.temp.right.value > vall:
                    if curr.left == AVLTree.temp or curr.right == AVLTree.temp:
                        AVLTree.temp.right = LL(AVLTree.temp.right)
                        curr.right = RR(AVLTree.temp)

        add(self.root, val)

        if self.root.max_height == 3 and self.root.left is None:
            if self.root.right.right is not None:
                self_temp = self.root.value
                self.root = self.root.right
                self.root.left = TreeNode(self_temp)
            if self.root.right.left is not None:
                self_temp_l = self.root
                self_temp_r = self.root.right
                self.root = self.root.right.left
                self.root.left = TreeNode(self_temp_l.value)
                self.root.right = TreeNode(self_temp_r.value)
        if self.root.max_height == 3 and self.root.right is None:
            if self.root.left.left is not None:
                self_temp = self.root.value
                self.root = self.root.left
                self.root.right = TreeNode(self_temp)
            if self.root.left.right is not None:
                self_temp_l = self.root.left
                self_temp_r = self.root
                self.root = self.root.left.right
                self.root.left = TreeNode(self_temp_l.value)
                self.root.right = TreeNode(self_temp_r.value)

    def to_list_bfs(self):
        res = []

        q = Queue()
        curr = self.root
        while curr is not None:
            if curr.left is not None:
                q.put(curr.left)
            if curr.right is not None:
                q.put(curr.right)
            res.append(curr.value)
            if q.empty():
                break
            else:
                curr = q.get()
        return res

