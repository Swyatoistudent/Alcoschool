class TrieNode:
    def __init__(self, symbol=None, next_symbol=None,end =False):

        if next_symbol is None:
            next_symbol = [i * 0 for i in range(127)]

        self.symbol = symbol
        self.next_symbol = next_symbol
        self.end = end
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self,word):
        curr = self.root
        for i in word:
            if i not in curr.next_symbol:
                curr.next_symbol[ord(i)] = TrieNode(i)
                curr =curr.next_symbol[ord(i)]
        curr.end = True
    def find(self,word):
        curr = self.root
        for i in word:
            charter = ord(i)
            if curr.next_symbol[ord(i)]!=0:
                curr = curr.next_symbol[ord(i)]
            elif i !=None:
                return False

        return curr.end



l1 = Trie()
l1.add("abbb")
print(l1.find("abbb"))