class TrieNode:
    def __init__(self,):
        self.is_end=False
        self.children=[None for _ in range(26)]

class Trie:
    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for char in word:
            if not cur.children[ord(char.lower())-97]:
                cur.children[ord(char.lower())-97]=TrieNode()
            cur=cur.children[ord(char.lower())-97]
        cur.is_end=True
            

    def search(self, word: str) -> bool:
        cur=self.root
        for char in word:
            if not cur.children[ord(char.lower())-97]:
                return False
            cur=cur.children[ord(char.lower())-97]
        return True if cur.is_end else False

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for char in prefix:
            if not cur.children[ord(char.lower())-97]:
                return False
            cur=cur.children[ord(char.lower())-97]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)