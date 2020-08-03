class List_Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class Linked_list:

    def __init__(self):
        self.head = None

    def prepend(self, value):
        self.head = List_Node(value, self.head)

    def append(self, value):
        curr = self.head
        if curr is None:
            self.head = List_Node(value,None)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = List_Node(value, None)

    def len(self):
        res = 0
        curr = self.head
        while curr is not None:
            res += 1
            curr = curr.next
        return res

    def to_list(self):
        res = []
        curr = self.head
        while curr is not None:
            res.append(curr.value)
            curr = curr.next
        return res
