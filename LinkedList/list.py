class List_Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        '''add elem after this index'''

    def add_elem_index(self, num, value):
        l1 = self
        i = 0
        while i < num:
            if self.next is None:
                break
            lis = self.next
            i += 1
        l2 = List_Node(value, l1.next)
        self.next = l2

    '''add elem in "tail" '''

    def add_elem_tail(self, value):
        while self.next is not None:
            self = self.next
        self.next = List_Node(value, None)
    '''delete elem by index'''
    def delete_elem_index(self, index):
        l1 = self
        l2 = l1.next
        i = 0
        while i < index - 1:
            if l2.next is None:
                return None
            l1 = l1.next
            l2 = l2.next
            i += 1
        l1.next = l2.next

    def delete_tail(self):
        while self.next.next is not None:
            self = self.next
        self.next = None



