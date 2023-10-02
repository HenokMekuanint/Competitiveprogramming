class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.index = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, i):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
            node.index.append(i)
    
    def starts_with(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return []
            node = node.children[index]
        return node.index
            
class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix = Trie()
        self.suffix = Trie()
        
        for i, word in enumerate(words):
            self.prefix.insert(word, i)
            self.suffix.insert(word[::-1], i)

    def f(self, pref: str, suff: str) -> int:
        
        p_list = self.prefix.starts_with(pref)
        s_list = self.suffix.starts_with(suff[::-1])
        
        i, j = len(p_list) - 1, len(s_list) - 1
        while i >= 0 and j >= 0:
            if p_list[i] == s_list[j]:
                return p_list[i]
            elif p_list[i] > s_list[j]:
                i -= 1
            else:
                j -= 1
        
        return -1
   
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)