from queue import Queue


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class BinSearchTree:
    def __init__(self):
        self.head = None

    def to_list_dfs(self, mode):  # mode : pre, in, post

        t = self.head
        res = []
        d = 0

        def dfs1(tree):
            if tree is None:
                return None
            if mode == "pre":
                res.append(tree.value)

            dfs1(tree.left)
            if mode == "in":
                res.append(tree.value)
            dfs1(tree.right)
            if mode == "post":
                res.append(tree.value)

        dfs1(t)
        return res

    def to_list_bfs(self):
        res = []
        q = Queue()
        curr = self.head
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


l1 = BinSearchTree()
l1.add(13)
l1.add(10)
l1.add(15)
l1.add(16)
l1.add(5)
l1.add(11)
l1.add(4)
l1.add(6)
l1.add(3)
res = l1.to_list_dfs("post")
print(res)


