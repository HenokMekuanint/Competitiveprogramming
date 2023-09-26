class TrieNode:
    def __init__(self):
        self.is_start=False
        self.is_end=False
        self.children=[None for _ in range(26)]
    
    

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for char in word:
            
            if not cur.children[ord(char.lower())-97]:
                cur.children[ord(char.lower())-97]=TrieNode()

            cur=cur.children[ord(char.lower())-97]
        cur.is_end=True

                
        

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end

            char = word[i]

            if char == '.':
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False

            if not node.children[ord(char.lower()) - 97]:
                return False

            return dfs(node.children[ord(char.lower()) - 97], i + 1)

        return dfs(self.root, 0)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)