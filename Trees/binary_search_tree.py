from queue import Queue


class TreeNode:
    def __init__(self, value, left, right):
        self.left = left
        self.right = right
        self.value = value


class BinSearchTree:
    def __init__(self):
        self.head = None

    def dfs(self):
        t = self.head

        def dfs1(tree):
            if tree is None:
                return None
            print(tree.value)
            dfs1(tree.left)
            dfs1(tree.right)

        dfs1(t)

    def bfs(self):

        q = Queue()
        curr = self.head
        while curr is not None:
            if curr.left is not None:
                q.put(curr.left)
            if curr.right is not None:
                q.put(curr.right)
            print(curr.value)
            if q.empty():
                break
            else:
                curr = q.get()

    def to_list(self):

        t = self.head
        res = []

        def dfs1(tree):
            if tree is None:
                return None
            res.append(tree.value)
            dfs1(tree.left)
            dfs1(tree.right)

        dfs1(t)
        return res

    def add(self, val):
        curr = self.head

        if curr is None:
            self.head = TreeNode(val, None, None)
            return self.head

        while curr is not None:
            if val > curr.value:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val, None, None)
                    break
            else:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val, None, None)
                    break
